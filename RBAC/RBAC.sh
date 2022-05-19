## AdminOperationsTeam

#Generate ket for Team X
openssl genrsa -out adminOperationsTeam.key 2048
#Create a certificate signing request containing the public key
openssl req -new -key adminOperationsTeam.key -out adminOperationsTeam.csr -subj "/CN=steam/O=adminOperationsTeam"
export adminOperationsTeamCSR=$(cat adminOperationsTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
#Sign this CSR using the root Kubernetes CA
kubectl apply -f CertificateSigningRequestSigned.yaml
#Inspect the new certificate
kubectl describe csr adminOperationsTeam
#Approve
kubectl certificate approve adminOperationsTeam
#Register the new credentials and config context
kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.crt --client-key=adminOperationsTeam.key
#Create New Context
export CLUSTER=$(kubectl config current-context)
kubectl config set-context adminOperationsTeam@$CLUSTER --cluster=$CLUSTER --user=adminOperationsTeam
kubectl config get-contexts
kubectl config current-context
kubectl apply -f Roles.yaml
kubectl create rolebinding adminoperations --user=adminOperationsTeam

## userManagementTeam

openssl genrsa -out userManagementTeam.key 2048
#Create a certificate signing request containing the public key
openssl req -new -key userManagementTeam.key -out userManagementTeam.csr -subj "/CN=steam/O=userManagementTeam"
export userManagementTeam=$(cat userManagementTeam.csr | base64 | tr -d '\n')
envsubst < "CertificateSigningRequest.yaml" > "CertificateSigningRequestSigned.yaml"
#Sign this CSR using the root Kubernetes CA
kubectl apply -f CertificateSigningRequestSigned.yaml
#Inspect the new certificate
kubectl describe csr userManagementTeam
#Approve
kubectl certificate approve userManagementTeam
#Register the new credentials and config context
kubectl config set-credentials userManagementTeam --client-certificate=userManagementTeam.crt --client-key=userManagementTeam.key
#Create New Context
export CLUSTER=$(kubectl config current-context)
kubectl config set-context userManagementTeam@$CLUSTER --cluster=$CLUSTER --user=userManagementTeam
kubectl config get-contexts
kubectl config current-context
kubectl apply -f Roles.yaml
kubectl create rolebinding userManagement --user=userManagementTeam