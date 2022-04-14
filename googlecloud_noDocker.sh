# Only use this file if you already have the docker images inside google cloud.
# If you change microservices code, use the other script

# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --num-nodes 2 --zone europe-west4-a

gcloud auth configure-docker

cd MicroServices

# Deploy
gcloud auth configure-docker

# Kubernetes Apply YAML files
kubectl apply -f mongo-secrets.yaml
kubectl apply -f pv.yaml
envsubst < "deployment.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml

cd ..

# Prometheus & Grafana
cd Prometheus

kubectl apply -f components.yaml
kubectl create configmap prometheus-cm --from-file prometheus-cm.yaml
kubectl apply -f prometheus.yaml
kubectl apply -f grafana.yaml

kubectl get pods