cfssl gencert -initca ca-csr.json | cfssljson -bare caSuggestions

cfssl gencert -ca=caSuggestions.pem -ca-key=caSuggestions-key.pem -config=ca-config.json -hostname='suggestionsserver' server-csr.json | cfssljson -bare serverSuggestions

cfssl gencert -ca=caSuggestions.pem -ca-key=caSuggestions-key.pem -config=ca-config.json client-csr.json | cfssljson -bare clientSuggestions

