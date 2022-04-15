export PROJECT_ID=$(gcloud info --format='value(config.project)')

envsubst < "deploymentDB.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml