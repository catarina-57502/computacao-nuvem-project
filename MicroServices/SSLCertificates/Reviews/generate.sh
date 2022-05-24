cfssl gencert -initca ca-csr.json | cfssljson -bare caReviews

cfssl gencert -ca=caReviews.pem -ca-key=caReviews-key.pem -config=ca-config.json -hostname='reviews-server-s' server-csr.json | cfssljson -bare serverReviews

cfssl gencert -ca=caReviews.pem -ca-key=caReviews-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientReviews

