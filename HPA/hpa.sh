# HPA
kubectl autoscale deployment adminoperationsserver --namespace=adminoperations --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment adminoperationsapi --namespace=adminoperations --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment usermanagementserver-deployment --namespace=usermanagement --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment usermanagementapi --namespace=usermanagement --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment libraryserver --namespace=library --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment libraryapi --namespace=library --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment wishlistserver --namespace=wishlist --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment wishlistapi --namespace=wishlist --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment suggestionsserver --namespace=suggestions --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment suggestionsapi --namespace=suggestions --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment searchesserver --namespace=searches --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment searchesapi --namespace=searches --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment reviews-api-d --namespace=reviews --cpu-percent=30 --min=1 --max=3
kubectl autoscale deployment reviews-server-d --namespace=reviews --cpu-percent=30 --min=1 --max=3

kubectl autoscale deployment logging-server-d --namespace=logging --cpu-percent=30 --min=1 --max=3

kubectl get hpa