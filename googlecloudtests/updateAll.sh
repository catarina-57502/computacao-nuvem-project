kubectl set image deployment/adminoperationsserver adminoperationsserver=adminoperationsserver:latest

kubectl set image deployment/adminoperationsapi adminoperationsapi=adminoperationsapi:latest

kubectl set image deployment/usermanagementserver usermanagementserver=usermanagementserver:latest

kubectl set image deployment/usermanagementapi usermanagementapi=usermanagementapi:latest

kubectl set image deployment/libraryserver libraryserver=libraryserver:latest

kubectl set image deployment/libraryapi libraryapi=libraryapi:latest

kubectl set image deployment/wishlistserver wishlistserver=wishlistserver:latest

kubectl set image deployment/wishlistapi wishlistapi=wishlistapi:latest

kubectl set image deployment/suggestionsserver suggestionsserver=suggestionsserver:latest

kubectl set image deployment/suggestionsapi suggestionsapi=suggestionsapi:latest

kubectl set image deployment/searchesserver searchesserver=searchesserver:latest

kubectl set image deployment/searchesapi searchesapi=searchesapi:latest

kubectl set image deployment/reviews-api reviews-api=reviews-api:latest

kubectl set image deployment/reviews-server reviews-server=reviews-server:latest