# Config
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone europe-west4-a --num-nodes 1 --enable-autoscaling --min-nodes 1 --max-nodes 1 --enable-autorepair

gcloud auth configure-docker

cd MicroServices

cd SSLCertificates
chmod u+x certificatesCloud.sh
./certificatesCloud.sh

cd ..

chmod u+x dockerBuildPush.sh
./dockerBuildPush.sh

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

kubectl create secret generic mongo-secretdb --from-file=MONGO_INITDB_ROOT_USERNAME=./username.txt --from-file=MONGO_INITDB_ROOT_PASSWORD=./password.txt

kubectl create secret generic mongo-secret --namespace=usermanagement --from-file=username=./username.txt --from-file=password=./password.txt
kubectl create secret generic mongo-secret --namespace=adminoperations --from-file=username=./username.txt --from-file=password=./password.txt


kubectl apply -f pv.yaml
envsubst < "deployment.yaml" > "deploymentENV.yaml"
kubectl apply -f deploymentENV.yaml

cd ..
cd Networking
chmod u+x network.sh
./network.sh

cd ..
cd HPA
chmod u+x hpa.sh
./hpa.sh

cd ..
cd Prometheus
chmod u+x prometheus.sh
./prometheus.sh

cd ..
cd RBAC

cd Team-AdminOperations
chmod u+x RBAC_AdminOperations.sh
./RBAC_AdminOperations.sh
cd ..

cd Team-UserManagement
chmod u+x RBAC_UserManagement.sh
./RBAC_UserManagement.sh
cd ..

cd Team-Library
chmod u+x RBAC_Library.sh
./RBAC_Library.sh
cd ..

cd Team-Wishlist
chmod u+x RBAC_Wishlist.sh
./RBAC_Wishlist.sh
cd ..

cd Team-Reviews
chmod u+x RBAC_Reviews.sh
./RBAC_Reviews.sh
cd ..

cd Team-Logging
chmod u+x RBAC_Logging.sh
./RBAC_Logging.sh
cd ..

cd Team-Searches
chmod u+x RBAC_Searches.sh
./RBAC_Searches.sh
cd ..

cd Team-Suggestions
chmod u+x RBAC_Suggestions.sh
./RBAC_Suggestions.sh

cd ..

cd ..
