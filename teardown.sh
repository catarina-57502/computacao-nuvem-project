# Delete the ingress resource object
kubectl delete -f MicroServices/ingress.yaml

# Delete the NGINX Ingress Helm chart
helm del nginx-ingress

# Delete the NGINX Ingress Helm chart repository
helm repo remove ingress-nginx

# Delete the Google Kubernetes Engine cluster
gcloud container clusters delete cluster-steam --zone=europe-west4-a
