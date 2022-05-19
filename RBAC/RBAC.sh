#Generate ket for Team X
openssl genrsa -out adminOperationsTeam.key 2048

#Create a certificate signing request containing the public key
openssl req -new -key adminOperationsTeam.key -out adminOperationsTeam.csr -subj "/CN=steam/O=adminOperationsTeam"

#Sign this CSR using the root Kubernetes CA
kubectl apply -f CertificateSigningRequest.yaml

#Inspect the new certificate
kubectl describe csr adminOperationsTeam

#Approve
kubectl certificate approve adminOperationsTeam

#Register the new credentials and config context
kubectl config set-credentials adminOperationsTeam --client-certificate=adminOperationsTeam.crt --client- key=adminOperationsTeam.key


kubectl config set-context adminOperationsTeam@kubernetes --cluster=kubernetes --user=adminOperationsTeam
