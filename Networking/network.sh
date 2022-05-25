# Add the nginx-stable Helm repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update


helm install nginx-ingress ingress-nginx/ingress-nginx \
    --set controller.publishService.enabled=true \
    --set controller.service.externalTrafficPolicy=Local \
    --set controller.service.annotations."service\.beta\.kubernetes\.io/do-loadbalancer-enable-proxy-protocol=true" \
    --set-string controller.config.use-proxy-protocol=true,controller.config.use-forward-headers=true,controller.config.compute-full-forward-for=true

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
