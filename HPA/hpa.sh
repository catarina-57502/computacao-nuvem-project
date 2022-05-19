# HPA
kubectl autoscale deployment adminoperationsserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment adminoperationsapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment usermanagementserver-deployment --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment libraryserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment libraryapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment wishlistserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment wishlistapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment suggestionsserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment suggestionsapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment searchesserver --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment searchesapi --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment reviews-api-d --cpu-percent=70 --min=1 --max=3
kubectl autoscale deployment reviews-server-d --cpu-percent=70 --min=1 --max=3

kubectl get hpa