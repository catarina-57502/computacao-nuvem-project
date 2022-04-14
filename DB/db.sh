export PROJECT_ID=$(gcloud info --format='value(config.project)')
pip install requests
cd app
cd csvFiles

python google_drive.py 1bfl997anVVA77yXs0cM3tC44vAn9mrUt ./csvFiles

cd csvFiles

sudo apt install unzip
unzip csvFiles.zip

cd ..
cd ..

docker build . -f app/Dockerfile -t writedb
docker tag writedb gcr.io/${PROJECT_ID}/writedb
docker push gcr.io/${PROJECT_ID}/writedb

envsubst < "deploymentDB.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml



