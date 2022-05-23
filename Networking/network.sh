# Add the nginx-stable Helm repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

# Deploy an NGINX controller Deployment and Service
helm install nginx-ingress ingress-nginx/ingress-nginx

echo "10s"
sleep 10s
echo "10s"
sleep 10s
echo "10s"
sleep 10s
echo "10s"
sleep 10s
echo "10s"
sleep 10s
echo "10s"
sleep 10s

# Apply the ingress resource to the cluster
kubectl apply -f external-names.yaml
kubectl apply -f ingress-namespaces.yaml
kubectl apply -f network-policies.yaml
