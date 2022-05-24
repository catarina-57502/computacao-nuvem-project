echo 'google admin secrets get'
gcloud secrets versions access 1 --secret="caAdminOperations" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caAdminOperations.pem
gcloud secrets versions access 1 --secret="serverAdminOperations" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverAdminOperations.pem
gcloud secrets versions access 1 --secret="serverAdminOperations-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverAdminOperations-key.pem
echo 'google lib secrets get'
gcloud secrets versions access 1 --secret="caLibrary" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caLibrary.pem
gcloud secrets versions access 1 --secret="serverLibrary" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverLibrary.pem
gcloud secrets versions access 1 --secret="serverLibrary-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverLibrary-key.pem
echo 'google logging secrets get'
gcloud secrets versions access 1 --secret="caLogging" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caLogging.pem
gcloud secrets versions access 1 --secret="serverLogging" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverLogging.pem
gcloud secrets versions access 1 --secret="serverLogging-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverLogging-key.pem
echo 'google reviews secrets get'
gcloud secrets versions access 1 --secret="caReviews" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caReviews.pem
gcloud secrets versions access 1 --secret="serverReviews" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverReviews.pem
gcloud secrets versions access 1 --secret="serverReviews-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverReviews-key.pem
echo 'google searches secrets get'
gcloud secrets versions access 1 --secret="caSearches" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caSearches.pem
gcloud secrets versions access 1 --secret="serverSearches" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverSearches.pem
gcloud secrets versions access 1 --secret="serverSearches-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverSearches-key.pem
echo 'google suggestions secrets get'
gcloud secrets versions access 1 --secret="caSuggestions" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caSuggestions.pem
gcloud secrets versions access 1 --secret="serverSuggestions" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverSuggestions.pem
gcloud secrets versions access 1 --secret="serverSuggestions-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverSuggestions-key.pem
echo 'google usermana secrets get'
gcloud secrets versions access 1 --secret="caUserManagement" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caUserManagement.pem
gcloud secrets versions access 1 --secret="serverUserManagement" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverUserManagement.pem
gcloud secrets versions access 1 --secret="serverUserManagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverUserManagement-key.pem
echo 'google wishlist secrets get'
gcloud secrets versions access 1 --secret="caWishlist" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > caWishlist.pem
gcloud secrets versions access 1 --secret="serverWishlist" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverWishlist.pem
gcloud secrets versions access 1 --secret="serverWishlist-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > serverWishlist-key.pem
echo 'copy files 1 to 1 SERVER'
cp caAdminOperations.pem ../adminOperations/server
cp serverAdminOperations.pem ../adminOperations/server
cp serverAdminOperations-key.pem ../adminOperations/server

cp caLibrary.pem ../library/server
cp serverLibrary.pem ../library/server
cp serverLibrary-key.pem ../library/server

cp caLogging.pem ../logging/server
cp serverLogging.pem ../logging/server
cp serverLogging-key.pem ../logging/server

cp caReviews.pem ../reviews/server
cp serverReviews.pem ../reviews/server
cp serverReviews-key.pem ../reviews/server

cp caSearches.pem ../searches/server
cp serverSearches.pem ../searches/server
cp serverSearches-key.pem ../searches/server

cp caSuggestions.pem ../suggestions/server
cp serverSuggestions.pem ../suggestions/server
cp serverSuggestions-key.pem ../suggestions/server

cp caUserManagement.pem ../userManagement/server
cp serverUserManagement.pem ../userManagement/server
cp serverUserManagement-key.pem ../userManagement/server

cp caWishlist.pem ../wishlist/server
cp serverWishlist.pem ../wishlist/server
cp serverWishlist-key.pem ../wishlist/server

echo 'copy files 1 to All User'
cp caUserManagement.pem ../adminOperations/server
cp serverUserManagement.pem ../adminOperations/server
cp serverUserManagement-key.pem ../adminOperations/server

cp caUserManagement.pem ../library/server
cp serverUserManagement.pem ../library/server
cp serverUserManagement-key.pem ../library/server

cp caUserManagement.pem ../logging/server
cp serverUserManagement.pem ../logging/server
cp serverUserManagement-key.pem ../logging/server

cp caUserManagement.pem ../reviews/server
cp serverUserManagement.pem ../reviews/server
cp serverUserManagement-key.pem ../reviews/server

cp caUserManagement.pem ../searches/server
cp serverUserManagement.pem ../searches/server
cp serverUserManagement-key.pem ../searches/server

cp caUserManagement.pem ../suggestions/server
cp serverUserManagement.pem ../suggestions/server
cp serverUserManagement-key.pem ../suggestions/server

cp caUserManagement.pem ../wishlist/server
cp serverUserManagement.pem ../wishlist/server
cp serverUserManagement-key.pem ../wishlist/server

echo 'copy files 1 to All Logging'
cp caLogging.pem ../adminOperations/server
cp serverLogging.pem ../adminOperations/server
cp serverLogging-key.pem ../adminOperations/server

cp caLogging.pem ../library/server
cp serverLogging.pem ../library/server
cp serverLogging-key.pem ../library/server

cp caLogging.pem ../reviews/server
cp serverLogging.pem ../reviews/server
cp serverLogging-key.pem ../reviews/server

cp caLogging.pem ../searches/server
cp serverLogging.pem ../searches/server
cp serverLogging-key.pem ../searches/server

cp caLogging.pem ../suggestions/server
cp serverLogging.pem ../suggestions/server
cp serverLogging-key.pem ../suggestions/server

cp caLogging.pem ../userManagement/server
cp serverLogging.pem ../userManagement/server
cp serverLogging-key.pem ../userManagement/server

cp caLogging.pem ../wishlist/server
cp serverLogging.pem ../wishlist/server
cp serverLogging-key.pem ../wishlist/server

echo 'copy files 1 to All special cases'

cp caSearches.pem ../library/server
cp serverSearches.pem ../library/server
cp serverSearches-key.pem ../library/server

cp caSearches.pem ../wishlist/server
cp serverSearches.pem ../wishlist/server
cp serverSearches-key.pem ../wishlist/server

echo 'copy files 1 to 1 API'
cp caAdminOperations.pem ../adminOperations/api
cp serverAdminOperations.pem ../adminOperations/api
cp serverAdminOperations-key.pem ../adminOperations/api

cp caLibrary.pem ../library/api
cp serverLibrary.pem ../library/api
cp serverLibrary-key.pem ../library/api

cp caLogging.pem ../logging/api
cp serverLogging.pem ../logging/api
cp serverLogging-key.pem ../logging/api

cp caReviews.pem ../reviews/api
cp serverReviews.pem ../reviews/api
cp serverReviews-key.pem ../reviews/api

cp caSearches.pem ../searches/api
cp serverSearches.pem ../searches/api
cp serverSearches-key.pem ../searches/api

cp caSuggestions.pem ../suggestions/api
cp serverSuggestions.pem ../suggestions/api
cp serverSuggestions-key.pem ../suggestions/api

cp caUserManagement.pem ../userManagement/api
cp serverUserManagement.pem ../userManagement/api
cp serverUserManagement-key.pem ../userManagement/api

cp caWishlist.pem ../wishlist/api
cp serverWishlist.pem ../wishlist/api
cp serverWishlist-key.pem ../wishlist/api

echo 'copy files 1 to All User'
cp caUserManagement.pem ../adminOperations/api
cp serverUserManagement.pem ../adminOperations/api
cp serverUserManagement-key.pem ../adminOperations/api

cp caUserManagement.pem ../library/api
cp serverUserManagement.pem ../library/api
cp serverUserManagement-key.pem ../library/api

cp caUserManagement.pem ../logging/api
cp serverUserManagement.pem ../logging/api
cp serverUserManagement-key.pem ../logging/api

cp caUserManagement.pem ../reviews/api
cp serverUserManagement.pem ../reviews/api
cp serverUserManagement-key.pem ../reviews/api

cp caUserManagement.pem ../searches/api
cp serverUserManagement.pem ../searches/api
cp serverUserManagement-key.pem ../searches/api

cp caUserManagement.pem ../suggestions/api
cp serverUserManagement.pem ../suggestions/api
cp serverUserManagement-key.pem ../suggestions/api

cp caUserManagement.pem ../wishlist/api
cp serverUserManagement.pem ../wishlist/api
cp serverUserManagement-key.pem ../wishlist/api

echo 'copy files 1 to All Logging'
cp caLogging.pem ../adminOperations/api
cp serverLogging.pem ../adminOperations/api
cp serverLogging-key.pem ../adminOperations/api

cp caLogging.pem ../library/api
cp serverLogging.pem ../library/api
cp serverLogging-key.pem ../library/api

cp caLogging.pem ../reviews/api
cp serverLogging.pem ../reviews/api
cp serverLogging-key.pem ../reviews/api

cp caLogging.pem ../searches/api
cp serverLogging.pem ../searches/api
cp serverLogging-key.pem ../searches/api

cp caLogging.pem ../suggestions/api
cp serverLogging.pem ../suggestions/api
cp serverLogging-key.pem ../suggestions/api

cp caLogging.pem ../userManagement/api
cp serverLogging.pem ../userManagement/api
cp serverLogging-key.pem ../userManagement/api

cp caLogging.pem ../wishlist/api
cp serverLogging.pem ../wishlist/api
cp serverLogging-key.pem ../wishlist/api

echo 'copy files 1 to All special cases'

cp caSearches.pem ../library/api
cp serverSearches.pem ../library/api
cp serverSearches-key.pem ../library/api

cp caSearches.pem ../wishlist/api
cp serverSearches.pem ../wishlist/api
cp serverSearches-key.pem ../wishlist/api