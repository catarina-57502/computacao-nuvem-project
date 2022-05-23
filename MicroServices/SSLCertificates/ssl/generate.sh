sudo apt update
sudo apt install golang-cfssl
# CA Certificate and Config
cfssl gencert -initca ca-csr.json | cfssljson -bare ca
#Server and Client certificates
cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -hostname='adminoperationsserver' server-csr.json | cfssljson -bare server
cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json client-csr.json | cfssljson -bare client

mv server-key.pem /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/server
mv server.pem /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/server
mv ca.pem  /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/api

