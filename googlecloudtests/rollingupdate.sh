cd ..

kubectl set image deployment/libraryapi libraryapi=wishlistapi
kubectl rollout status deployment/libraryapi
PID=$!
sleep 2
kill $PID
kubectl get rs
kubectl describe deployment
kubectl rollout history deployment/libraryapi
kubectl rollout history deployment/libraryapi --revision=2