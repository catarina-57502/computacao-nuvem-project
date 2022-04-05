# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone=europe-west4-a --num-nodes=1
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

# Deploy
gcloud auth configure-docker

kubectl get nodes
kubectl apply -f deployment.yaml --env=PROJECT_ID=${PROJECT_ID}
kubectl get pods