import requests
from Hero import Hero
import sys

auth = open("auth.txt", "r")

headers = {
    "Accept": "application/json",
    "authorization": f"{auth.read()}"
}
def main():
    # 9LR9QY98 || LC22V09C9 || 2VPGP0LV
    try:
        player_tag = sys.argv[1]
    except IndexError:
        print("Please provide a player tag")
        print("usage:")
        print("./Clash_of_Clans_API.py <player_tag>")
        sys.exit()

    try:
        return account_information(player_tag)
    except TypeError:
        print(f"Invalid player tag provided: {player_tag}")
        sys.exit()

def print_player_info(result):
    print("Hello " + result.get("player_name") + "!")
    print("Your Town Hall Level is " + result.get("th_level"))
    print("")

def print_player_heroes(result):
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

def print_player_pets(result):
    if len(result.get("pet_levels")) == 0:
        print("You currently have no pets, upgrade to TH14 to unlock!")
    else:
        print("You also have " + str(len(result.get("pet_levels"))) + " pets.")
        for j in range(len(result.get("pet_levels"))):
            print("Your " + result.get("pet_names")[j] + " is currently Level " + result.get("pet_levels")[j])

def print_output(result):
    print('==========================================================================')
    print_player_info(result)
    print_player_heroes(result)
    print_player_pets(result)

def account_information(player_tag):
    """Return info about user account"""
    url = "https://api.clashofclans.com/v1/players/%23" + player_tag

    api_response = requests.get(url, headers=headers)
    if api_response.status_code != 200:
        raise TypeError
    response_json = api_response.json()

    player_name = response_json.get("name")
    th_level = str(response_json.get("townHallLevel"))
    heroes_response = response_json.get("heroes")
    player_heroes = []



    for i in range(len(heroes_response)):
        if heroes_response[i]["village"] == "home":
            player_heroes.append(
                Hero(
                    heroes_response[i]["name"],
                    heroes_response[i]["level"],
                    heroes_response[i]["maxLevel"],
                )
            )

    pet_names = ["L.A.S.S.I", "Mighty Yak", "Electro Owl", "Unicorn"]
    pet_levels = []
    for j in range(len(response_json.get("troops"))):
        if response_json.get("troops")[j].get("name") in pet_names:
            pet_levels.append(str(response_json.get("troops")[j].get("level")))

    return {
        "player_name": player_name,
        "th_level": th_level,
        "player_heroes": player_heroes,
        "pet_levels": pet_levels,
        "pet_names": pet_names
        }

print_output(main())