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

### To populate the db

```
cd DB
sh db.sh
```
Note: If you already have the docker images of the db just run:  
```
sh db_noDocker.sh
```

### To use the services API

Export the EXTERNAL-IP of the NGINX ingress controller in a variable:

```
export NGINX_INGRESS_IP=$(kubectl get service nginx-ingress-ingress-nginx-controller -ojson | jq -r '.status.loadBalancer.ingress[].ip')
```

Ensure that you have the correct IP address value stored in the $NGINX_INGRESS_IP variable
```
echo $NGINX_INGRESS_IP
```

Access the web application by going to the:
```
http://$NGINX_INGRESS_IP.nip.io/[SERVICE_ENDPOINT]
```

### To setup Grafana Dashboard

```
http://$GRAFANA_IP:3000/
```
1. Open Configurations - Data Sources - Add Data Source - Prometheus
2. URL: http://$PROMETHEUS_IP:9090/
3. Save & Test
4. Dashboard - Import - Import file from **Prometheus directory** - *grafanaDashboard.json*

Note: Sometimes the graphs are empty you need to open the graph on the dashboard and set the Data Source again
1. Edit - Data Source - Prometheus(deafult)

You can check:
1. Number of requests for each microservices
2. Time of the request for each microservices
3. CPU usage per pod
4. Memory usage per pod

### Clean up

```
sh teardown.sh
```

### Links Dataset

https://www.kaggle.com/najzeko/steam-reviews-2021   
https://www.kaggle.com/trolukovich/steam-games-complete-dataset  

## Elementos do Grupo

André Grilo  
Catarina Moita  
Martim Mourão  
Thomas Marques  
Tomás Dias  

### Organização

1. System and API Architect (CEO) - Martim
2. Networking  - Catarina
3. Security Specialist - Thomas
4. DevOps Officer - Tomas
5. Data Scientist - Andre

### Microservices 

Martim Mourão - Admin Operations & User Management  
CatarinaMoita - WishList & Library  
Tomás Dias  - Reviews  
Thomas Marques  - Suggestions  
André Grilo - Searchs  


# Google Cloud

(1) deploy the containers to a kubernetes cluster on the cloud (ALL)  

(2) deploy the databases to Kubernetes volumes - (Catarina)  

(3) use an HTTP(s) ingress to connect each external service to the cloud load balancer  (Tomas)  

(4) configure kubernetes policy for scalability (HPA and if required VPA and Cluster)  (Thomas)  

(5) expose only the services that really need to be accessed from the outside (ALL)  

(6) use a managed authentication service and implement the planned authorization policies (Martim)  

(7) configure resource utilization through requests and limits (try to be as cost-effective as possible) (ALL)  

(8) setup metrics per pod for monitoring with Prometheus (Martim)  

(9) setup your own probes for liveness, readiness and start-up (Grilo)  

(10) implement rolling updates and rollback (Catarina)  

# Security


Check the need for config maps (Todos)  
Actions with Git CA (Martim)  



1. Managing multiple namespaces. Create different RBAC policies for each namespace.  
    (TODOS)  
    a. Criar namespace para o seu microserviço  
    b. Role para seu microserviço  
    c. ClusterRole para seu microserviço  
    d. RoleBinding para seu microserviço  
    Referencia: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
2. Check if the current configuration of the network architecture isolates critical points from the public Internet. (Grilo)
3. Secure channels in all communications. (Martim)
4. Creation of logs (Audit Logging). (Tomas)
5. Creation of NetworkPolicy. (Catarina)
6. Protection for DoS, each request needs an access token, to monitor maximum requests per user. (Martim/Catarina)
7. Check for attack Broken Object Level Authorization (when sensitive fields within an object are incorrectly exposed),
   test for database inputs injection. (Thomas)
