import requests
from Hero import Hero

auth = open("auth.txt", "r")

headers = {
    "Accept": "application/json",
    "authorization": f"{auth.read()}"
}

def print_player_info():
    print("Hello " + result.get("player_name") + "!")
    print("Your Town Hall Level is " + result.get("th_level"))
    print("")

def print_player_heroes():
    heroes_list = result.get("player_heroes")
    if len(heroes_list) == 0:
        print("You do not have any heroes! Upgrade to  TH7 to unlock the Barbarian King!")
    elif len(heroes_list) == 1:
        print("You have 1 hero! Upgrade to TH9 to unlock the Archer Queen!")
    elif len(heroes_list) == 2:
        print("You have 2 heroes! Upgrade to TH11 to unlock the Grand Warden!")
    elif len(heroes_list) == 3:
        print("You have 3 heroes! Upgrade to TH13 to unlock the Royal Champion!")
    else:
        print("You have 4 heroes!")
    for i in range(len(heroes_list)):
        print("Your " + heroes_list[i].name + " is currently Level " + str(heroes_list[i].level) + heroes_list[i].print_max_message())
    print("")

def print_player_pets():
    if len(result.get("pet_levels")) == 0:
        print("You currently have no pets, upgrade to TH14 to unlock!")
    else:
        print("You also have " + str(len(result.get("pet_levels"))) + " pets.")
        for j in range(len(result.get("pet_levels"))):
            print("Your " + result.get("pet_names")[j] + " is currently Level " + result.get("pet_levels")[j])

def print_output():
    print('==========================================================================')
    print_player_info()
    print_player_heroes()
    print_player_pets()

def account_information():
    """Return info about user account"""
    # player_tag = input("Enter your player tag (without the #, not case sensitive): ").upper() #"LC22V09C9" #"9LR9QY98"  #
    url = "https://api.clashofclans.com/v1/players/%23lc22v09c9"

    request = requests.get(url, headers=headers)
    response = request.json()

    player_name = response.get("name")
    th_level = str(response.get("townHallLevel"))
    heroes_response = response.get("heroes")
    player_heroes = []

    for i in range(len(heroes_response)):
        if heroes_response[i]["village"] == "home":
            player_heroes.append(
                Hero(
                    heroes_response[i]["name"],
                    heroes_response[i]["level"],
                    heroes_response[i]["maxLevel"],
                    heroes_response[i]["village"]
                )
            )

    pet_names = ["L.A.S.S.I", "Mighty Yak", "Electro Owl", "Unicorn"]
    pet_levels = []
    for j in range(len(response.get("troops"))):
        if response.get("troops")[j].get("name") in pet_names:
            pet_levels.append(str(response.get("troops")[j].get("level")))
    
    return {
        "player_name": player_name,
        "th_level": th_level,
        "player_heroes": player_heroes,
        "pet_levels": pet_levels,
        "pet_names": pet_names
        }

result = account_information()

print_output()