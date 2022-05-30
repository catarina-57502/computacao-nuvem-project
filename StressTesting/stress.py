import requests
import time

ip = input("Enter IP: ")
nRequest = input("Enter Number Request Send: ")
timeSleep = input("Enter Time: ")

userManagementURL = "http://" + ip + "/user/login"
adminURL = "http://" + ip + "/admin/games"
libraryURL = "http://" + ip + "/library"
reviewsURL = "http://" + ip + "/reviews"
searchesURL = "http://" + ip + "/searches/reviews"
suggestionsURL = "http://" + ip + "/suggestions/games"
wishesURL = "http://" + ip + "/wishes"

# Token
for i in range(int(nRequest)):
    PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
    userToken = requests.post(userManagementURL, json = PARAMS)
    print(userToken.json())
    time.sleep(float(timeSleep))