cfssl gencert -initca ca-csr.json | cfssljson -bare caLogging

cfssl gencert -ca=caLogging.pem -ca-key=caLogging-key.pem -config=ca-config.json -hostname='logging-server-s' server-csr.json | cfssljson -bare serverLogging

cfssl gencert -ca=caLogging.pem -ca-key=caLogging-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientLogging

