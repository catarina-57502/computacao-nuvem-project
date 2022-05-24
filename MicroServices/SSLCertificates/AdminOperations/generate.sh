cfssl gencert -initca ca-csr.json | cfssljson -bare caAdminOperations

cfssl gencert -ca=caAdminOperations.pem -ca-key=caAdminOperations-key.pem -config=ca-config.json -hostname='adminoperationsserver' server-csr.json | cfssljson -bare serverAdminOperations

cfssl gencert -ca=caAdminOperations.pem -ca-key=caAdminOperations-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientAdminOperations

