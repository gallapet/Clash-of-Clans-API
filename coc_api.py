import sys
from http import HTTPStatus
import requests

from Player_Special.Hero import Hero
from Player_Special.Troop import Troop

class InvalidTagError(ValueError):
    pass

class AuthenticationError(ValueError):
    pass

def main():
    try:
        player_tag = sys.argv[1]
    except IndexError:
        print("Please provide a player tag")
        print("usage:")
        print("./coc_api.py <player_tag>")
        sys.exit()

    try:
        response = account_information(player_tag)
    except InvalidTagError:
        print(f"Invalid player tag provided: {player_tag}")
        sys.exit()
    except AuthenticationError:
        print("Error within authorization key")
        sys.exit()

    print_lines()
    print_player_info(response)
    print_lines()
    print_player_heroes(response)
    print_lines()
    print_player_pets(response)
    print_lines()

def account_information(player_tag):
    """Return info about user account"""
    auth = open("auth.txt", "r")
    headers = {
        "Accept": "application/json",
        "authorization": f"{auth.read()}"
    }

    url = "https://api.clashofclans.com/v1/players/%23" + player_tag

    api_response = requests.get(url, headers=headers)
    if api_response.status_code == HTTPStatus.NOT_FOUND:
        raise InvalidTagError from ValueError
    elif api_response.status_code == HTTPStatus.FORBIDDEN:
        raise AuthenticationError from ValueError
    response_json = api_response.json()

    return response_json

def get_player_name(response):
    return response.get("name")

def get_town_hall_level(response):
    return response.get("townHallLevel")

def print_player_info(response):
    print(f"Hello {get_player_name(response)}!")
    print(f"Your current Town Hall Level is {get_town_hall_level(response)}")

def get_player_heroes(response):
    return [Hero(hero["name"], hero["level"], hero["maxLevel"])
            for hero in response.get("heroes") if hero["village"] == "home"]

def print_player_heroes(response):
    player_heroes = get_player_heroes(response)

    if len(player_heroes) == 0:
        print("You do not have any heroes! Upgrade to  TH7 to unlock the Barbarian King!")
    elif len(player_heroes) == 1:
        print("You have 1 hero! Upgrade to TH9 to unlock the Archer Queen!")
    elif len(player_heroes) == 2:
        print("You have 2 heroes! Upgrade to TH11 to unlock the Grand Warden!")
    elif len(player_heroes) == 3:
        print("You have 3 heroes! Upgrade to TH13 to unlock the Royal Champion!")
    else:
        print("You have 4 heroes!")
    for hero in range(len(player_heroes)):
        print(f"Your {player_heroes[hero].name} is currently Level {player_heroes[hero].level}{player_heroes[hero].print_max_message()}")

def print_player_pets(response):
    troops_response = response.get("troops")
    pet_names = ["L.A.S.S.I", "Electro Owl", "Mighty Yak", "Unicorn",
                 "Frosty", "Diggy", "Poison Lizard", "Phoenix",
                 "Spirit Fox", "Angry Jelly"]
    troops = []
    for troop in troops_response:
        if troop["name"] in pet_names:
            troops.append(
                Troop(
                    name=troop["name"],
                    level=troop["level"]
                )
            )

    pet_list = [None] * len(troops)
    for pet in troops:
        if pet.name in pet_names:
            pet_list[pet_names.index(pet.name)] = pet
    if len(pet_list) == 0:
        print("You currently have no pets, upgrade to TH14 to unlock!")
    else:
        print(f"You also have {len(pet_list)} pets.")
        for pet in pet_list:
            print(f"Your {pet.name} is currently Level {pet.level}")

def print_lines():
    print("===================================================================================")

if __name__ == "__main__":
    main()
