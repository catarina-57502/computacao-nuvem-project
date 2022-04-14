export PROJECT_ID=$(gcloud info --format='value(config.project)')
pip install gdown
pip install --upgrade gdown

cd app
cd csvFiles

gdown https://drive.google.com/file/d/1bfl997anVVA77yXs0cM3tC44vAn9mrUt/view?usp=sharing

apt install unzip
unzip csvFiles.zip

cd ..
cd ..

docker build . -f app/Dockerfile -t writedb
docker tag writedb gcr.io/${PROJECT_ID}/writedb
docker push gcr.io/${PROJECT_ID}/writedb

envsubst < "deploymentDB.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml



