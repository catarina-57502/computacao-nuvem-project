openssl genrsa -out adminOperationsTeam.key 2048
openssl req -new -key adminOperationsTeam.key -out adminOperationsTeam.csr -subj "/CN=adminOperationsTeam/O=adminOperationsTeam"

openssl genrsa -out userManagementTeam.key 2048
openssl req -new -key userManagementTeam.key -out userManagementTeam.csr -subj "/CN=userManagementTeam/O=userManagementTeam"

kubectl auth can-i '*' '*'
kubectl auth can-i create pods --all-namespaces

cat ~/.kube/config
rm -r ~/.kube/config

kubectl config use-context adminOperationsTeam


kubectl config get-contexts
kubectl config current-context

gcloud secrets versions access 1 --secret="adminTeam-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="adminTeam-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d