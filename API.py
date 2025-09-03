# looks easy for now, but if I understand correctly. The website should also be prepared for this
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to get Info. Problem Code: {response.status_code}")

pokemon_name = input("What pokemon would you like to know more about? \n").lower()
pokemon_info = get_info(pokemon_name)

if pokemon_info:
    print(f"Name:   {pokemon_info["name"].upper()}")
    print(f"ID:     {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")