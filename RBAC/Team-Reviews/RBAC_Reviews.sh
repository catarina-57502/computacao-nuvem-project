echo 'Starting RBAC - Team Reviews'

gcloud secrets versions access 1 --secret="reviews-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > reviewsTeam.key
gcloud secrets versions access 1 --secret="reviews-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > reviewsTeam.csr

export CLUSTER=$(kubectl config current-context)

export reviewsTeamCSR=$(cat reviewsTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestReviews.yaml" > "CertificateSigningRequestReviewsSigned.yaml"

kubectl apply -f CertificateSigningRequestReviewsSigned.yaml

kubectl describe csr reviewsTeam
kubectl certificate approve reviewsTeam

kubectl get csr reviewsTeam -o jsonpath='{.status.certificate}'| base64 -d > reviewsTeam.crt

kubectl config set-credentials reviewsTeam --client-certificate=reviewsTeam.crt --client-key=reviewsTeam.key

kubectl apply -f RolesReviews.yaml
kubectl apply -f RoleBindingReviews.yaml

kubectl config set-context reviewsTeam --cluster=$CLUSTER --namespace=reviews --user=reviewsTeam


echo 'End RBAC - Team Reviews'