echo 'Starting RBAC - Team Suggestions'

gcloud secrets versions access 1 --secret="suggestions-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > suggestionsTeam.key
gcloud secrets versions access 1 --secret="suggestions-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > suggestionsTeam.csr

export CLUSTER=$(kubectl config current-context)

export suggestionsTeamCSR=$(cat suggestionsTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestSuggestions.yaml" > "CertificateSigningRequestSuggestionsSigned.yaml"

kubectl apply -f CertificateSigningRequestSuggestionsSigned.yaml

kubectl describe csr suggestionsTeam
kubectl certificate approve suggestionsTeam

kubectl get csr suggestionsTeam -o jsonpath='{.status.certificate}'| base64 -d > suggestionsTeam.crt

kubectl config set-credentials suggestionsTeam --client-certificate=suggestionsTeam.crt --client-key=suggestionsTeam.key

kubectl apply -f RolesSuggestions.yaml
kubectl apply -f RoleBindingSuggestions.yaml

kubectl config set-context suggestionsTeam --cluster=$CLUSTER --namespace=suggestions --user=suggestionsTeam


echo 'End RBAC - Team Suggestions'