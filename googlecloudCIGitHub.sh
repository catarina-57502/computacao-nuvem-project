# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone europe-west4-a --num-nodes 1 --enable-autoscaling --min-nodes 1 --max-nodes 1 --enable-autorepair

gcloud auth configure-docker

cd ConfigMaps

kubectl create configmap --from-file configMapMicroServices.yaml

cd ..
cd MicroServices

# Kubernetes Apply YAML files
kubectl apply -f mongo-secrets.yaml
kubectl apply -f pv.yaml
envsubst < "deployment.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml

# HPA
kubectl autoscale deployment adminoperationsserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment adminoperationsapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment usermanagementserver-deployment --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment libraryserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment libraryapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment wishlistserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment wishlistapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment suggestionsserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment suggestionsapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment searchesserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment searchesapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment reviews-api-d --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment reviews-server-d --cpu-percent=70 --min=1 --max=3

kubectl get hpa

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
kubectl apply -f ingress.yaml

cd ..
cd Prometheus

kubectl apply -f components.yaml
kubectl create configmap prometheus-cm --from-file prometheus-cm.yaml
kubectl apply -f prometheus.yaml
kubectl apply -f grafana.yaml

kubectl get pods