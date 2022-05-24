cfssl gencert -initca ca-csr.json | cfssljson -bare caWishlist

cfssl gencert -ca=caWishlist.pem -ca-key=caWishlist-key.pem -config=ca-config.json -hostname='wishlistserver' server-csr.json | cfssljson -bare serverWishlist

cfssl gencert -ca=caWishlist.pem -ca-key=caWishlist-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientWishlist

