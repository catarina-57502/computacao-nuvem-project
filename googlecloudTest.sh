# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam2 --zone europe-west4-a --num-nodes 2 --enable-autoscaling --min-nodes 1 --max-nodes 3 --enable-autorepair

gcloud auth configure-docker

cd MicroServices

cd SSLCertificates
chmod u+x certificatesCloud.sh
./certificatesCloud.sh

cd ..

cd ..
cd NameSpaces
chmod u+x namespaces.sh
./namespaces.sh

cd ..
cd ConfigMaps
chmod u+x configmaps.sh
./configmaps.sh

cd ..
cd MicroServices

export username=$(gcloud secrets versions access 1 --secret="username" --format='get(payload.data)' | tr '_-' '/+' | base64 -d)
export password=$(gcloud secrets versions access 1 --secret="password" --format='get(payload.data)' | tr '_-' '/+' | base64 -d)

envsubst < "mongo-secrets.yaml" > "mongo-secretsENV.yaml"
kubectl apply -f mongo-secretsENV.yaml

kubectl apply -f pv.yaml
envsubst < "deployment.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml

cd ..
cd Networking
chmod u+x network.sh
./network.sh


cd ..
cd Prometheus
chmod u+x prometheus.sh
./prometheus.sh

