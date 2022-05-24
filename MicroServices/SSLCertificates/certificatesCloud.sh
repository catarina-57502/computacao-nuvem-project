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
echo 'copy files 1 to 1'
cp caAdminOperations.pem ../adminOperations/keys
cp serverAdminOperations.pem ../adminOperations/keys
cp serverAdminOperations-key.pem ../adminOperations/keys

cp caLibrary.pem ../library/keys
cp serverLibrary.pem ../library/keys
cp serverLibrary-key.pem ../library/keys

cp caLogging.pem ../logging/keys
cp serverLogging.pem ../logging/keys
cp serverLogging-key.pem ../logging/keys

cp caReviews.pem ../reviews/keys
cp serverReviews.pem ../reviews/keys
cp serverReviews-key.pem ../reviews/keys

cp caSearches.pem ../searches/keys
cp serverSearches.pem ../searches/keys
cp serverSearches-key.pem ../searches/keys

cp caSuggestions.pem ../suggestions/keys
cp serverSuggestions.pem ../suggestions/keys
cp serverSuggestions-key.pem ../suggestions/keys

cp caUserManagement.pem ../userManagement/keys
cp serverUserManagement.pem ../userManagement/keys
cp serverUserManagement-key.pem ../userManagement/keys

cp caWishlist.pem ../wishlist/keys
cp serverWishlist.pem ../wishlist/keys
cp serverWishlist-key.pem ../wishlist/keys

echo 'copy files 1 to All User'
cp caUserManagement.pem ../adminOperations/keys
cp serverUserManagement.pem ../adminOperations/keys
cp serverUserManagement-key.pem ../adminOperations/keys

cp caUserManagement.pem ../library/keys
cp serverUserManagement.pem ../library/keys
cp serverUserManagement-key.pem ../library/keys

cp caUserManagement.pem ../logging/keys
cp serverUserManagement.pem ../logging/keys
cp serverUserManagement-key.pem ../logging/keys

cp caUserManagement.pem ../reviews/keys
cp serverUserManagement.pem ../reviews/keys
cp serverUserManagement-key.pem ../reviews/keys

cp caUserManagement.pem ../searches/keys
cp serverUserManagement.pem ../searches/keys
cp serverUserManagement-key.pem ../searches/keys

cp caUserManagement.pem ../suggestions/keys
cp serverUserManagement.pem ../suggestions/keys
cp serverUserManagement-key.pem ../suggestions/keys

cp caUserManagement.pem ../wishlist/keys
cp serverUserManagement.pem ../wishlist/keys
cp serverUserManagement-key.pem ../wishlist/keys

echo 'copy files 1 to All Logging'
cp caLogging.pem ../adminOperations/keys
cp serverLogging.pem ../adminOperations/keys
cp serverLogging-key.pem ../adminOperations/keys

cp caLogging.pem ../library/keys
cp serverLogging.pem ../library/keys
cp serverLogging-key.pem ../library/keys

cp caLogging.pem ../reviews/keys
cp serverLogging.pem ../reviews/keys
cp serverLogging-key.pem ../reviews/keys

cp caLogging.pem ../searches/keys
cp serverLogging.pem ../searches/keys
cp serverLogging-key.pem ../searches/keys

cp caLogging.pem ../suggestions/keys
cp serverLogging.pem ../suggestions/keys
cp serverLogging-key.pem ../suggestions/keys

cp caLogging.pem ../userManagement/keys
cp serverLogging.pem ../userManagement/keys
cp serverLogging-key.pem ../userManagement/keys

cp caLogging.pem ../wishlist/keys
cp serverLogging.pem ../wishlist/keys
cp serverLogging-key.pem ../wishlist/keys

echo 'copy files 1 to All special cases'

cp caSearches.pem ../library/keys
cp serverSearches.pem ../library/keys
cp serverSearches-key.pem ../library/keys

cp caSearches.pem ../wishlist/keys
cp serverSearches.pem ../wishlist/keys
cp serverSearches-key.pem ../wishlist/keys