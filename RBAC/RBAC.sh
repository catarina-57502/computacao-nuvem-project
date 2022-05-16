kube-apiserver --authorization-mode=Security,RBAC

#Generate ket for Team X
openssl genrsa -out adminOperationsTeam.key 2048

#Create a certificate signing request containing the public key
openssl req -new -key adminOperationsTeam.key -out adminOperationsTeam.csr -subj "/CN=steam/O=adminOperationsTeam"

#Sign this CSR using the root Kubernetes CA
openssl x509 -req -in adminOperationsTeam.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out adminOperationsTeam.crt

#Inspect the new certificate
openssl x509 -in adminOperationsTeam.crt -text

#Register the new credentials and config context
kubectl config set-credentials adminOperationsTeam --client-certificate=/home/teams/adminOperationsTeam.crt --client- key=/home/teams/adminOperationsTeam.key
kubectl config set-context adminOperationsTeam@kubernetes --cluster=kubernetes --user=adminOperationsTeam
