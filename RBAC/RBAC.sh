# AdminOperationsTeam
echo 'Starting RBAC'
gcloud secrets versions access 1 --secret="adminoperations-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.key
gcloud secrets versions access 1 --secret="adminoperations-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > adminOperationsTeam.csr
echo 'Keys loaded'
export adminOperationsTeamCSR=$(cat adminOperationsTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
#Sign this CSR using the root Kubernetes CA
kubectl apply -f CertificateSigningRequestSigned.yaml
#Inspect the new certificate
kubectl describe csr adminOperationsTeam
#Approve
kubectl certificate approve adminOperationsTeam
#Register the new credentials and config context
kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.csr --client-key=adminOperationsTeam.key
#Create New Context
export CLUSTER=$(kubectl config current-context)
kubectl config set-context adminOperationsTeam@$CLUSTER --cluster=$CLUSTER --user=adminOperationsTeam
kubectl config get-contexts
kubectl config current-context
kubectl apply -f Roles.yaml
kubectl create rolebinding adminoperations --user=adminOperationsTeam

# UserManagementTeam
gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.key
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagementTeam.csr

export userManagementTeam=$(cat userManagementTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
#Sign this CSR using the root Kubernetes CA
kubectl apply -f CertificateSigningRequestSigned.yaml
#Inspect the new certificate
kubectl describe csr userManagementTeam
#Approve
kubectl certificate approve userManagementTeam
#Register the new credentials and config context
kubectl config set-credentials userManagementTeam --client-certificate=userManagementTeam.csr --client-key=userManagementTeam.key
#Create New Context
export CLUSTER=$(kubectl config current-context)
kubectl config set-context userManagementTeam@$CLUSTER --cluster=$CLUSTER --user=userManagementTeam
kubectl config get-contexts
kubectl config current-context
kubectl apply -f Roles.yaml
kubectl create rolebinding userManagement --user=userManagementTeam

echo 'RBAC end'