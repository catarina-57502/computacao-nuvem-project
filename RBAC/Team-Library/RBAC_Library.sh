echo 'Starting RBAC - Team Library'

gcloud secrets versions access 1 --secret="library-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > libraryTeam.key
gcloud secrets versions access 1 --secret="library-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > libraryTeam.csr

export CLUSTER=$(kubectl config current-context)

export libraryTeamCSR=$(cat libraryTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestLibrary.yaml" > "CertificateSigningRequestLibrarySigned.yaml"

kubectl apply -f CertificateSigningRequestLibrarySigned.yaml

kubectl describe csr libraryTeam
kubectl certificate approve libraryTeam

kubectl get csr libraryTeam -o jsonpath='{.status.certificate}'| base64 -d > libraryTeam.crt

kubectl config set-credentials libraryTeam --client-certificate=libraryTeam.crt --client-key=libraryTeam.key

kubectl apply -f RolesLibrary.yaml
kubectl apply -f RoleBindingLibrary.yaml

kubectl config set-context libraryTeam --cluster=$CLUSTER --namespace=library --user=libraryTeam


echo 'End RBAC - Team Library'