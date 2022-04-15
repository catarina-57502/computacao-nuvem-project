# Project Cloud

The goal of the project is to develop a cloud native application that offers a set of services that provide
relevant information extracted from a dataset. The services will be provided through a REST API.

## To deploy on the CLOUD!

Create a Project on google cloud  
Open gcloud shell:   
```
git clone https://github.com/mdmourao/CloudProjectGroup7  
cd CloudProjectGroup7  
sh googlecloud.sh  
```

Note: If you already have the docker images pushed to the container registry just run:  
```
sh googlecloud_noDocker.sh
```

## To populate the db

```
cd DB
sh db.sh
```
Note: If you already have the docker images of the db just run:  
```
sh db_noDocker.sh
```

## To use the services api

Export the EXTERNAL-IP of the NGINX ingress controller in a variable:

```
export NGINX_INGRESS_IP=$(kubectl get service nginx-ingress-ingress-nginx-controller -ojson | jq -r '.status.loadBalancer.ingress[].ip')

echo $NGINX_INGRESS_IP
```
Access the web application by going to the:
```
http://$NGINX_INGRESS_IP.nip.io/[SERVICE_NAME]
```

## Links Dataset

https://www.kaggle.com/najzeko/steam-reviews-2021   
https://www.kaggle.com/trolukovich/steam-games-complete-dataset  

## Elementos do Grupo

André Grilo  
Catarina Moita  
Martim Mourão  
Thomas Marques  
Tomás Dias  

## Organização

1. System and API Architect (CEO) - Martim
2. Networking  - Catarina
3. Security Specialist - Thomas
4. DevOps Officer - Tomas
5. Data Scientist - Andre

## Microservices 

Martim Mourão - Admin Operations & User Management  
CatarinaMoita - WishList & Library  
Tomás Dias  - Reviews  
Thomas Marques  - Suggestions  
André Grilo - Searchs  


## Google Cloud

(1) deploy the containers to a kubernetes cluster on the cloud (ALL)  

(2) deploy the databases to Kubernetes volumes - (Catarina)  

(3) use an HTTP(s) ingress to connect each external service to the cloud load balancer  (Tomas)  

(4) configure kubernetes policy for scalability (HPA and if required VPA and Cluster)  (Thomas)  

(5) expose only the services that really need to be accessed from the outside (ALL)  

(6) use a managed authentication service and implement the planned authorization policies (Martim)  

(7) configure resource utilization through requests and limits (try to be as cost-effective as possible) (ALL)  

(8) setup metrics per pod for monitoring with Prometheus (Martim)  

(9) setup your own probes for liveness, readiness and start-up (Grilo)  

<<<<<<< HEAD
(10) implement rolling updates and rollback (Catarina)  
=======
(10) implement rolling updates and rollback (Catarina)  
>>>>>>> 20bffeab9f5124d851bb1c2f6f29cb2b3859f3a6
