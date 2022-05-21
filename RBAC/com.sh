kubectl config set-cluster default-cluster --server=https://<host ip>:6443 --certificate-authority <path-to-kubernetes-ca> --embed-certs
kubectl config set-credentials <credential-name> --client-key <path-to-key>.pem --client-certificate <path-to-cert>.pem --embed-certs
kubectl config set-context default-system --cluster default-cluster --user <credential-name>
kubectl config use-context default-system

# Check to see if I can do everything in my current namespace ("*" means all)
kubectl auth can-i '*' '*'

# Check to see if I can create pods in any namespace
kubectl auth can-i create pods --all-namespaces


kubectl config use-context adminOperationsTeam@gke_phase4-cn_europe-west4-a_cluster-steam


gcloud secrets versions access 1 --secret="adminTeam-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="adminTeam-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d
gcloud secrets versions access 1 --secret="usermanagement-cert" --format='get(payload.data)' | tr '_-' '/+' | base64 -d