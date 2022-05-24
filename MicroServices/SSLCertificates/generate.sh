openssl req -x509 -newkey rsa:4096 -days 365 -nodes -keyout ca-key.pem -out ca-cert.pem -subj "/C=PT/ST=Lisbon/L=FCUL/O=FCUL/OU=Education/CN=adminoperationsserver"

openssl x509 -in ca-cert.pem -noout -text

openssl req -newkey rsa:4096 -nodes -keyout server-key.pem -out server-req.pem -subj "/C=PT/ST=Lisbon/L=FCUL/O=FCUL/OU=Education/CN=adminoperationsserver"

openssl x509 -req -in server-req.pem -days 60 -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -extfile server-ext.cnf

openssl req -newkey rsa:4096 -nodes -keyout client-key.pem -out client-req.pem -subj "/C=PT/ST=Lisbon/L=FCUL/O=FCUL/OU=Education/CN=adminoperationsserver"

openssl x509 -req -in client-req.pem -days 60 -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out client-cert.pem -extfile server-ext.cnf

openssl x509 -in server-cert.pem -noout -text