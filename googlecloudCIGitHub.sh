# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone europe-west4-a --num-nodes 1 --enable-autoscaling --min-nodes 1 --max-nodes 1 --enable-autorepair

gcloud auth configure-docker

cd MicroServices

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
echo "admin" | base64 > username.txt
echo "admin" | base64 > password.txt
kubectl create secret generic mongo-secrets --from-file=./username.txt --from-file=./password.txt

kubectl apply -f pv.yaml
envsubst < "deployment.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml

cd ..
cd Networking
chmod u+x network.sh
./network.sh

cd..
cd HPA
chmod u+x hpa.sh
./hpa.sh

cd..
cd Networking
chmod u+x network.sh
./network.sh

cd ..
cd Prometheus
chmod u+x prometheus.sh
./prometheus.sh