kubectl apply -f components.yaml
kubectl create configmap prometheus-cm --from-file prometheus-cm.yaml
kubectl apply -f prometheus.yaml
kubectl apply -f grafana.yaml
