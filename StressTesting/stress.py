import requests


ip = input("Enter IP: ")
print(ip)

nRequest = input("Enter Number Request Send: ")
print(nRequest)

userManagementURL = "http://" + ip + "/user/login"
adminURL = "http://" + ip + "/admin/games"
libraryURL = "http://" + ip + "/library"
reviewsURL = "http://" + ip + "/reviews"
searchesURL = "http://" + ip + "/searches/reviews"
suggestionsURL = "http://" + ip + "/suggestions/games"
wishesURL = "http://" + ip + "/wishes"

# Token
PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
userToken = requests.get(url = userManagementURL, data = PARAMS)

print(userToken)