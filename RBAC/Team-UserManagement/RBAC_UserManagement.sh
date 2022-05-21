echo 'Starting RBAC - userManagement'

gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagement.key
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagement.csr

export CLUSTER=$(kubectl config current-context)

export userManagementCSR=$(cat userManagement.csr | base64 | tr -d '\n')

envsubst < "CertificateSigningRequestUserManagement.yaml" > "CertificateSigningRequestUserManagementSigned.yaml"

kubectl apply -f CertificateSigningRequestUserManagementSigned.yaml

kubectl describe csr userManagementTeam
kubectl certificate approve userManagementTeam

kubectl get csr userManagementTeam -o jsonpath='{.status.certificate}'| base64 -d > userManagement.crt

kubectl config set-credentials userManagementTeam --client-certificate=userManagement.crt --client-key=userManagement.key

kubectl apply -f RolesUserManagement.yaml
kubectl apply -f RoleBindingUserManagement.yaml

kubectl config set-context userManagementTeam --cluster=$CLUSTER --namespace=usermanagement --user=userManagementTeam


echo 'End RBAC - userManagementTeam'