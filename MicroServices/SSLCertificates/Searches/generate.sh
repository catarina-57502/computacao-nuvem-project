cfssl gencert -initca ca-csr.json | cfssljson -bare caSearches

cfssl gencert -ca=caSearches.pem -ca-key=caSearches-key.pem -config=ca-config.json -hostname='searchesserver' server-csr.json | cfssljson -bare serverSearches

cfssl gencert -ca=caSearches.pem -ca-key=caSearches-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientSearches

