cd ..

kubectl rollout undo deployment/libraryapi
kubectl get deployment libraryapi