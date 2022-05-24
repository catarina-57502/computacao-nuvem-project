echo 'Starting RBAC - Team Searches'

gcloud secrets versions access 1 --secret="searches-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > searchesTeam.key
gcloud secrets versions access 1 --secret="searches-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > searchesTeam.csr

export CLUSTER=$(kubectl config current-context)

export searchesTeamCSR=$(cat searchesTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestSearches.yaml" > "CertificateSigningRequestSearchesSigned.yaml"

kubectl apply -f CertificateSigningRequestSearchesSigned.yaml

kubectl describe csr searchesTeam
kubectl certificate approve searchesTeam

kubectl get csr searchesTeam -o jsonpath='{.status.certificate}'| base64 -d > searchesTeam.crt

kubectl config set-credentials searchesTeam --client-certificate=searchesTeam.crt --client-key=searchesTeam.key

kubectl apply -f RolesSearches.yaml
kubectl apply -f RoleBindingSearches.yaml

kubectl config set-context searchesTeam --cluster=$CLUSTER --namespace=searches --user=searchesTeam


echo 'End RBAC - Team Searches'