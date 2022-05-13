
# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone europe-west4-a --num-nodes 2 --enable-autoscaling --min-nodes 1 --max-nodes 4 --enable-autorepair

gcloud auth configure-docker

cd MicroServices

# MicroService Admin Operations Server
cd adminOperations
docker build . -f server/Dockerfile -t adminoperationsserver
docker tag adminoperationsserver gcr.io/${PROJECT_ID}/adminoperationsserver
docker push gcr.io/${PROJECT_ID}/adminoperationsserver

# MicroService Admin Operations API
docker build . -f api/Dockerfile -t adminoperationsapi
docker tag adminoperationsapi gcr.io/${PROJECT_ID}/adminoperationsapi
docker push gcr.io/${PROJECT_ID}/adminoperationsapi

cd ..

# MicroService User Management Server
cd userManagement
docker build . -f server/Dockerfile -t usermanagementserver
docker tag usermanagementserver gcr.io/${PROJECT_ID}/usermanagementserver
docker push gcr.io/${PROJECT_ID}/usermanagementserver

# MicroService User Management API
docker build . -f api/Dockerfile -t usermanagementapi
docker tag usermanagementapi gcr.io/${PROJECT_ID}/usermanagementapi
docker push gcr.io/${PROJECT_ID}/usermanagementapi

cd ..

# MicroService Library Server
cd library
docker build . -f server/Dockerfile -t libraryserver
docker tag libraryserver gcr.io/${PROJECT_ID}/libraryserver
docker push gcr.io/${PROJECT_ID}/libraryserver

# MicroService Library API
docker build . -f api/Dockerfile -t libraryapi
docker tag libraryapi gcr.io/${PROJECT_ID}/libraryapi
docker push gcr.io/${PROJECT_ID}/libraryapi

cd ..

# MicroService Wishlist Server
cd wishlist
docker build . -f server/Dockerfile -t wishlistserver
docker tag wishlistserver gcr.io/${PROJECT_ID}/wishlistserver
docker push gcr.io/${PROJECT_ID}/wishlistserver

# MicroService Wishlist API
docker build . -f api/Dockerfile -t wishlistapi
docker tag wishlistapi gcr.io/${PROJECT_ID}/wishlistapi
docker push gcr.io/${PROJECT_ID}/wishlistapi

cd ..

# MicroService Suggestions Server
cd suggestions
docker build . -f server/Dockerfile -t suggestionsserver
docker tag suggestionsserver gcr.io/${PROJECT_ID}/suggestionsserver
docker push gcr.io/${PROJECT_ID}/suggestionsserver

# Microservice Suggestions API
docker build . -f api/Dockerfile -t suggestionsapi
docker tag suggestionsapi gcr.io/${PROJECT_ID}/suggestionsapi
docker push gcr.io/${PROJECT_ID}/suggestionsapi

cd ..

# MicroService Searches Server
cd searches
docker build . -f server/Dockerfile -t searchesserver
docker tag searchesserver gcr.io/${PROJECT_ID}/searchesserver
docker push gcr.io/${PROJECT_ID}/searchesserver

# MicroService Searches API
docker build . -f api/Dockerfile -t searchesapi
docker tag searchesapi gcr.io/${PROJECT_ID}/searchesapi
docker push gcr.io/${PROJECT_ID}/searchesapi

cd ..

# MicroService Reviews Server
cd reviews
docker build . -f server/Dockerfile -t gcr.io/${PROJECT_ID}/reviews-server
docker push gcr.io/${PROJECT_ID}/reviews-server

# MicroService Reviews API
docker build . -f api/Dockerfile -t gcr.io/${PROJECT_ID}/reviews-api
docker push gcr.io/${PROJECT_ID}/reviews-api

cd ..

# Deploy
gcloud auth configure-docker

cd ..
cd ConfigMaps

kubectl create dns --from-file configMapMicroServices.yaml

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
