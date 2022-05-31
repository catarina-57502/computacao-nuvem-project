import requests
import time
import threading




ip = input("Enter IP: ")
nThread = input("Enter Number Threads: ")
nRequest = input("Enter Number Request Send: ")
timeSleep = input("Enter Time: ")

userManagementURL = "http://" + ip + "/user/login"
adminURL = "http://" + ip + "/admin/games"
libraryURL = "http://" + ip + "/library"
reviewsURL = "http://" + ip + "/reviews/85184605"
searchesURL = "http://" + ip + "/searches/games?genre=Indie,Simulation,Strategy"
suggestionsURL = "http://" + ip + "/suggestions/games?developer=id Software"
wishesURL = "http://" + ip + "/wishes"



PARAMS = {"email":"martimmourao@gmail.com","password":"qwerty"}
userToken = requests.post(userManagementURL, json = PARAMS)
userTokenFinal = userToken.json()

def stressAdmin():
    print("Start AdminOperations")
    for i in range(int(nRequest)):
        PARAMS = {
                   "url": "https://store.steampowered.com/app/379720/DOOM/",
                   "types": "app",
                   "name": "DOOM022222",
                   "desc_snippet": "Now includes all three premium DLC packs (Unto the Evil, Hell Followed, and Bloodfall), maps, modes, and weapons, as well as all feature updates including Arcade Mode, Photo Mode, and the latest Update 6.66, which brings further multiplayer improvements as well as revamps multiplayer progression.",
                   "recent_reviews": "Very Positive,(554),- 89% of the 554 user reviews in the last 30 days are positive.",
                   "all_reviews": "Very Positive,(42,550),- 92% of the 42,550 user reviews for this game are positive.",
                   "release_date": "May 12, 2016",
                   "developer": "id Software",
                   "publisher": "Bethesda Softworks,Bethesda Softworks",
                   "popular_tags": "FPS,Gore,Action,Demons,Shooter,First-Person,Great Soundtrack,Multiplayer,Singleplayer,Fast-Paced,Sci-fi,Horror,Classic,Atmospheric,Difficult,Blood,Remake,Zombies,Co-op,Memes",
                   "game_details": "Single-player,Multi-player,Co-op,Steam Achievements,Steam Trading Cards,Partial Controller Support,Steam Cloud",
                   "languages": "English,French,Italian,German,Spanish - Spain,Japanese,Polish,Portuguese - Brazil,Russian,Traditional Chinese",
                   "achievements": 54,
                   "genre": "Action",
                   "game_description": "About This Game Developed by id software, the studio that pioneered the first-person shooter genre and created multiplayer Deathmatch, DOOM returns as a brutally fun and challenging modern-day shooter experience. Relentless demons, impossibly destructive guns, and fast, fluid movement provide the foundation for intense, first-person combat – whether you’re obliterating demon hordes through the depths of Hell in the single-player campaign, or competing against your friends in numerous multiplayer modes. Expand your gameplay experience using DOOM SnapMap game editor to easily create, play, and share your content with the world. STORY: You’ve come here for a reason.",
                   "mature_content": "The developers describe the content like this:  This Game may contain content not appropriate for all ages, or may not be appropriate for viewing at work: Frequent Violence or Gore, General Mature Content",
                   "minimum_requirements": "Minimum:,OS:,Windows 7/8.1/10 (64-bit versions),Processor:,Intel Core i5-2400/AMD FX-8320 or better,Memory:,8 GB RAM,Graphics:,NVIDIA GTX 670 2GB/AMD Radeon HD 7870 2GB or better,Storage:,55 GB available space,Additional Notes:,Requires Steam activation and broadband internet connection for Multiplayer and SnapMap",
                   "recommended_requirements": "Recommended:,OS:,Windows 7/8.1/10 (64-bit versions),Processor:,Intel Core i7-3770/AMD FX-8350 or better,Memory:,8 GB RAM,Graphics:,NVIDIA GTX 970 4GB/AMD Radeon R9 290 4GB or better,Storage:,55 GB available space,Additional Notes:,Requires Steam activation and broadband internet connection for Multiplayer and SnapMap",
                   "original_price": "$19.99",
                   "discount_price": "$14.99"
                 }
        headers = {"token": userTokenFinal}
        editGame = requests.put(adminURL, headers=headers ,json = PARAMS)
        print(str(editGame) + "Admin")
        time.sleep(float(timeSleep))

def stressLib():
    print("Start Library")
    for i in range(int(nRequest)):
        headers = {"token": userTokenFinal}
        listLib = requests.get(libraryURL, headers=headers)
        print(str(listLib) + "Library")
        time.sleep(float(timeSleep))

def stressRev():
    print("Start Reviews")
    for i in range(int(nRequest)):
        listReviews = requests.get(reviewsURL)
        print(str(listReviews) + "Reviews")
        time.sleep(float(timeSleep))

def stressSea():
    print("Start Searches")
    for i in range(int(nRequest)):
        listGames = requests.get(searchesURL)
        print(str(listGames) + "Searches")
        time.sleep(float(timeSleep))

def stressSugg():
    print("Start Suggestions")
    for i in range(int(nRequest)):
        listSug = requests.get(suggestionsURL)
        print(str(listSug) + "Suggestions")
        time.sleep(float(timeSleep))

def stressWish():
    print("Start Wishlist")
    for i in range(int(nRequest)):
        headers = {"token": userTokenFinal}
        listWish = requests.get(wishesURL, headers=headers)
        print(str(listWish)+ "Wishlist")
        time.sleep(float(timeSleep))


if __name__ == "__main__":
    for i in range(int(nThread)):
        admin = threading.Thread(target=stressAdmin, args=())
        lib = threading.Thread(target=stressLib, args=())
        rev = threading.Thread(target=stressRev, args=())
        sea = threading.Thread(target=stressSea, args=())
        sugg = threading.Thread(target=stressSugg, args=())
        wish = threading.Thread(target=stressWish, args=())
        admin.start()
        lib.start()
        rev.start()
        sea.start()
        sugg.start()
        wish.start()
