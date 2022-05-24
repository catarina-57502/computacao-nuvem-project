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
# Deploy
gcloud auth configure-docker
