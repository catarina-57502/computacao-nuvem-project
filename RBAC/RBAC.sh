# AdminOperationsTeam
echo 'Starting RBAC'

gcloud secrets versions access 1 --secret="adminoperations-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.key
gcloud secrets versions access 1 --secret="adminoperations-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.csr

gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.key
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.csr

export CLUSTER=$(kubectl config current-context)

export adminOperationsTeamCSR=$(cat adminOperationsTeam.csr | base64 | tr -d '\n')
export userManagementTeamCSR=$(cat userManagementTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"

kubectl apply -f CertificateSigningRequestSigned.yaml

kubectl describe csr userManagementTeam
kubectl certificate approve userManagementTeam

kubectl describe csr adminOperationsTeam
kubectl certificate approve adminOperationsTeam

kubectl get csr userManagementTeam -o jsonpath='{.status.certificate}'| base64 -d > userManagementTeam.crt
kubectl get csr adminOperationsTeam -o jsonpath='{.status.certificate}'| base64 -d > adminOperationsTeam.crt

kubectl config set-credentials userManagementTeam --client-certificate=userManagementTeam.crt --client-key=userManagementTeam.key
kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.crt --client-key=adminOperationsTeam.key

kubectl apply -f Roles.yaml
kubectl apply -f RoleBinding.yaml

kubectl config set-context userManagementTeam@$CLUSTER --cluster=$CLUSTER --namespace=usermanagement --user=userManagementTeam
kubectl config set-context adminOperationsTeam@$CLUSTER --cluster=$CLUSTER --namespace=adminoperations --user=adminOperationsTeam

echo 'RBAC end'
