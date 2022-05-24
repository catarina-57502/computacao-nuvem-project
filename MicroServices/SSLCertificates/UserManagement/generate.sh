cfssl gencert -initca ca-csr.json | cfssljson -bare caUserManagement

cfssl gencert -ca=caUserManagement.pem -ca-key=caUserManagement-key.pem -config=ca-config.json -hostname='usermanagementserversvc' server-csr.json | cfssljson -bare serverUserManagement

cfssl gencert -ca=caUserManagement.pem -ca-key=caUserManagement-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientUserManagement

