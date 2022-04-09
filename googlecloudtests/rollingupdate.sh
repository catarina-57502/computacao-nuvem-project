cd ..

kubectl set image deployment/libraryapi libraryapi=wishlistapi
kubectl get rs
kubectl describe deployment
kubectl rollout history deployment/libraryapi
kubectl rollout history deployment/libraryapi --revision=2