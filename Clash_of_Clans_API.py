import requests

auth = open("auth.txt", "r")

headers = {
    "Accept" : "application/json",
    "authorization" : f"{auth.read()}"
}

def print_player_info():
    print("Hello " + account_information().get("player_name") + "!")
    print("Your Town Hall Level is " + account_information().get("th_level"))
    print("")

def print_player_heroes():
    print("You have " + str(len(account_information().get("hero_levels"))) + " heroes.")
    for i in range(len(account_information().get("hero_levels"))):
        print("Your " + account_information().get("hero_names")[i] + " is currently Level " + account_information().get("hero_levels")[i])
    print("")

def print_player_pets():
    if len(account_information().get("pet_levels")) == 0:
        print("You currently have no pets, upgrade to TH14 to unlock!")
    else:
        print("You also have " + str(len(account_information().get("pet_levels"))) + " pets.")
        for j in range(len(account_information().get("pet_levels"))):
            print("Your " + account_information().get("pet_names")[j] + " is currently Level " + account_information().get("pet_levels")[j])

def print_output():
    print('==========================================================================')
    print_player_info()
    print_player_heroes()
    print_player_pets()

def account_information():
    # Return info about user account
    # player_tag = input("Enter your player tag (without the #, not case sensitive): ").upper() #"LC22V09C9" #"9LR9QY98"  #
    url = "https://api.clashofclans.com/v1/players/%239LR9QY98"

    request = requests.get(url, headers=headers)
    json = request.json()

    player_name = json.get("name")
    th_level = str(json.get("townHallLevel"))
    
    hero_levels = []
    hero_names = []
    for i in range(len(json.get("heroes"))):
        hero_level = str(json.get("heroes")[i].get("level"))
        hero_name = json.get("heroes")[i].get("name")
        if json.get("heroes")[i].get("village") == "home":
            hero_levels.append(hero_level)
            hero_names.append(hero_name)

    pet_names = ["L.A.S.S.I", "Mighty Yak", "Electro Owl", "Unicorn"]
    pet_levels = []
    for j in range(len(json.get("troops"))):
        if json.get("troops")[j].get("name") in pet_names:
            pet_levels.append(str(json.get("troops")[j].get("level")))
    
    return {
        "player_name": player_name,
        "th_level": th_level,
        "hero_levels": hero_levels,
        "hero_names": hero_names,
        "pet_levels": pet_levels,
        "pet_names": pet_names
        }

print_output()




