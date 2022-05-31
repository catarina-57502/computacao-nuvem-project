import requests
import time

i = 0

ip = input("Enter IP: ")
userManagementURL = "http://" + ip + "/user/login"

for i in range(50):
    i += 1
    PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
    userToken = requests.post(userManagementURL, json = PARAMS)
    userTokenFinal = userToken.json()
    print("Request"  + str(i))