import requests

auth = open("auth.txt", "r")

headers = {
    "Accept" : "application/json",
    "authorization" : f"{auth.read()}"
}

def getAccountInfo():
    # Return info about user account
    playerTag = input("Enter your player tag (without the #, not case sensitive): ").upper() #"LC22V09C9" #"9LR9QY98"  # 
    url = "https://api.clashofclans.com/v1/players/%23" + playerTag

    request = requests.get(url, headers=headers)
    json = request.json()

    player_name = json.get("name")
    th_level = str(json.get("townHallLevel"))
    
    levels = []
    names = []
    for i in range(len(json.get("heroes"))):
        hero_level = str(json.get("heroes")[i].get("level"))
        hero_name = json.get("heroes")[i].get("name")
        if json.get("heroes")[i].get("village") == "home":
            levels.append(hero_level)
            names.append(hero_name)
    
    return {
        "player_name" : player_name,
        "th_level" : th_level,
        "levels" : levels,
        "names" : names
        }

results = getAccountInfo()
print('==========================================================================')
print("Hello " + results.get("player_name") + "!")
print("Your Town Hall Level is " + results.get("th_level"))
print("You have " + str(len(results.get("levels"))) + " heroes.")
for j in range(len(results.get("levels"))):
    print("Your " + results.get("names")[j] + " is currently Level " + results.get("levels")[j])