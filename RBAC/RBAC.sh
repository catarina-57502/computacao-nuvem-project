# AdminOperationsTeam
echo 'Starting RBAC'
gcloud secrets versions access 1 --secret="adminoperations-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.key
gcloud secrets versions access 1 --secret="adminoperations-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.csr
export adminOperationsTeamCSR=$(cat adminOperationsTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
kubectl apply -f CertificateSigningRequestSigned.yaml
kubectl describe csr adminOperationsTeam
kubectl certificate approve adminOperationsTeam
kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.csr --client-key=adminOperationsTeam.key
export CLUSTER=$(kubectl config current-context)
kubectl config set-context adminOperationsTeam@$CLUSTER --cluster=$CLUSTER --user=adminOperationsTeam
kubectl create rolebinding adminoperations --user=adminOperationsTeam

# UserManagementTeam
gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.key
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.csr
export userManagementTeamCSR=$(cat userManagementTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
kubectl apply -f CertificateSigningRequestSigned.yaml
kubectl describe csr userManagementTeam
kubectl certificate approve userManagementTeam
kubectl config set-credentials userManagementTeam --client-certificate=userManagementTeam.csr --client-key=userManagementTeam.key
export CLUSTER=$(kubectl config current-context)
kubectl config set-context userManagementTeam@$CLUSTER --cluster=$CLUSTER --user=userManagementTeam
kubectl create rolebinding userManagement --user=userManagementTeam

kubectl apply -f Roles.yaml
echo 'RBAC end'
