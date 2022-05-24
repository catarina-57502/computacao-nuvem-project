cfssl gencert -initca ca-csr.json | cfssljson -bare caLibrary

cfssl gencert -ca=caLibrary.pem -ca-key=caLibrary-key.pem -config=ca-config.json -hostname='libraryserver' server-csr.json | cfssljson -bare serverLibrary

cfssl gencert -ca=caLibrary.pem -ca-key=caLibrary-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientLibrary
cfssl gencert -ca=caLibrary.pem -ca-key=caLibrary-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientLibrary

