export PROJECT_ID=$(gcloud info --format='value(config.project)')

docker build . -f app/Dockerfile -t writedb
docker tag writedb gcr.io/${PROJECT_ID}/writedb
docker push gcr.io/${PROJECT_ID}/writedb

envsubst < "deploymentDB.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml



