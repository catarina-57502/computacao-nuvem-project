echo 'Starting RBAC - Team Logging'

gcloud secrets versions access 1 --secret="logging-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > loggingTeam.key
gcloud secrets versions access 1 --secret="logging-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > loggingTeam.csr

export CLUSTER=$(kubectl config current-context)

export loggingTeamCSR=$(cat loggingTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestLogging.yaml" > "CertificateSigningRequestLoggingSigned.yaml"

kubectl apply -f CertificateSigningRequestLoggingSigned.yaml

kubectl describe csr loggingTeam
kubectl certificate approve loggingTeam

kubectl get csr loggingTeam -o jsonpath='{.status.certificate}'| base64 -d > loggingTeam.crt

kubectl config set-credentials loggingTeam --client-certificate=loggingTeam.crt --client-key=loggingTeam.key

kubectl apply -f RolesLogging.yaml
kubectl apply -f RoleBindingLogging.yaml

kubectl config set-context loggingTeam --cluster=$CLUSTER --namespace=logging --user=loggingTeam


echo 'End RBAC - Team Logging'