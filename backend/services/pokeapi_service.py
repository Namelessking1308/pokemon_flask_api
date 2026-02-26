import requests

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_pokemon_data(name):
    response = requests.get(f"{POKEAPI_URL} {name.lower()}")

    if response.status_code != 200:
        return None
    
    data = response.json()

    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data ["stats"]}

    return{
        "name": data[name],
        "hp": stats.get("hp", 0),
        "attack": stats.get("attack", 0),
        "defense": stats.get("defense", 0),
        "sprite_url": data["sprites"] ["front_default"]
    }