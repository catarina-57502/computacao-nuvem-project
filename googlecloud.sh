# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone=europe-west4-a --num-nodes=1
gcloud auth configure-docker

cd CloudProjectGroup7
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

# Deploy
gcloud auth configure-docker

kubectl get nodes
kubectl apply -f deployment.yaml
kubectl get pods

