echo 'Starting RBAC - Team AdminOperations'

gcloud secrets versions access 1 --secret="adminoperations-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.key
gcloud secrets versions access 1 --secret="adminoperations-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.csr

export CLUSTER=$(kubectl config current-context)

export adminOperationsTeamCSR=$(cat adminOperationsTeam.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestAdminOperations.yaml" > "CertificateSigningRequestAdminOperationsSigned.yaml"

kubectl apply -f CertificateSigningRequestAdminOperationsSigned.yaml

kubectl describe csr adminOperationsTeam
kubectl certificate approve adminOperationsTeam

kubectl get csr adminOperationsTeam -o jsonpath='{.status.certificate}'| base64 -d > adminOperationsTeam.crt

kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.crt --client-key=adminOperationsTeam.key

kubectl apply -f Roles.yaml
kubectl apply -f RoleBinding.yaml

kubectl config set-context adminOperationsTeam --cluster=$CLUSTER --namespace=adminoperations --user=adminOperationsTeam


echo 'End RBAC - Team AdminOperations'