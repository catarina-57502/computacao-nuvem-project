echo 'Starting RBAC - Team Wishlist'

gcloud secrets versions access 1 --secret="wishlist-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > wishlistTeam.key
gcloud secrets versions access 1 --secret="wishlist-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > wishlistTeam.csr

export CLUSTER=$(kubectl config current-context)

export wishlistTeamCSR=$(cat wishlistTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestWishlist.yaml" > "CertificateSigningRequestWishlistSigned.yaml"

kubectl apply -f CertificateSigningRequestWishlistSigned.yaml

kubectl describe csr wishlistTeam
kubectl certificate approve wishlistTeam

kubectl get csr wishlistTeam -o jsonpath='{.status.certificate}'| base64 -d > wishlistTeam.crt

kubectl config set-credentials wishlistTeam --client-certificate=wishlistTeam.crt --client-key=wishlistTeam.key

kubectl apply -f RolesWishlist.yaml
kubectl apply -f RoleBindingWishlist.yaml

kubectl config set-context wishlistTeam --cluster=$CLUSTER --namespace=wishlist --user=wishlistTeam


echo 'End RBAC - Team Wishlist'