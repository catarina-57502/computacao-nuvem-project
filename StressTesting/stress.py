import requests
import time
import threading


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



PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
userToken = requests.post(userManagementURL, json = PARAMS)
userTokenFinal = userToken.json()

def stressUser():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressAdmin():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressLib():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressRev():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressSea():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressSugg():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))

def stressWish():
    # Stress Testing User Management
    for i in range(int(nRequest)):
        PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
        userToken = requests.post(userManagementURL, json = PARAMS)
        time.sleep(float(timeSleep))


if __name__ == "__main__":
    userM = threading.Thread(target=stressUser, args=())
    admin = threading.Thread(target=stressAdmin, args=())
    lib = threading.Thread(target=stressLib, args=())
    rev = threading.Thread(target=stressRev, args=())
    sea = threading.Thread(target=stressSea, args=())
    sugg = threading.Thread(target=stressSugg, args=())
    wish = threading.Thread(target=stressWish, args=())

    userM.start()
    admin.start()
    lib.start()
    rev.start()
    sea.start()
    sugg.start()
    wish.start()
