echo Generate CA key:
openssl genrsa -passout pass:4523 -des3 -out ca.key 4096

echo Generate CA certificate:
openssl req -passin pass:4523 -new -x509 -days 365 -key ca.key -out ca.crt -subj  "/C=PT/ST=LIS/L=SI/O=FCUL/OU=STEAM/CN=CA"

echo Generate server key:
openssl genrsa -passout pass:4523 -des3 -out server.key 4096

echo Generate server signing request:
openssl req -passin pass:4523 -new -key server.key -out server.csr -subj  "/C=PT/ST=LIS/L=SI/O=FCUL/OU=STEAM/CN=CA"


echo Self-sign server certificate:
openssl x509 -req -passin pass:4523 -days 365 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt

echo Remove passphrase from server key:
openssl rsa -passin pass:4523 -in server.key -out server.key

echo Generate client key
openssl genrsa -passout pass:4523 -des3 -out client.key 4096

echo Generate client signing request:
openssl req -passin pass:4523 -new -key client.key -out client.csr -subj  "/C=PT/ST=LIS/L=SI/O=FCUL/OU=STEAM/CN=CA"

echo Self-sign client certificate:
openssl x509 -passin pass:4523 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out client.crt

echo Remove passphrase from client key:
openssl rsa -passin pass:4523 -in client.key -out client.key


mv ca.crt /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/api
mv ca.crt /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/server

mv server.crt /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/server
mv server.key /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/server

mv client.crt /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/api
mv client.key /home/grupo7_cn_fcul/CloudProjectGroup7/MicroServices/adminOperations/api