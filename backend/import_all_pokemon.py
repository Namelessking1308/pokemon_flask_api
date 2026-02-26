import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from app import app
from models import db
from models.pokemon import Pokemon

session = requests.Session()
retry = Retry(
    total=5,                  
    backoff_factor=1,         
    status_forcelist=[429, 500, 502, 503, 504], 
    allowed_methods=["HEAD", "GET", "OPTIONS", "GET"]
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)


def fetch_pokemon_data(name):
    try:
        response = session.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code != 200:
            print(f"Pokémon {name} non trouvé ({response.status_code})")
            return None

        data = response.json()
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data.get("stats", [])}

        return {
            "name": data.get("name", ""),
            "hp": stats.get("hp", 0),
            "attack": stats.get("attack", 0),
            "defense": stats.get("defense", 0),
            "sprite_url": data.get("sprites", {}).get("front_default")
        }

    except Exception as e:
        print(f"Erreur pour {name}: {e}")
        return None

with app.app_context():
    response = session.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
    all_pokemon = response.json().get("results", [])

    print(f"{len(all_pokemon)} Pokémon trouvés, import en cours...")

    for i, p in enumerate(all_pokemon, start=1):
        data = fetch_pokemon_data(p["name"])
        if data:
            if not Pokemon.query.filter_by(name=data["name"]).first():
                pokemon = Pokemon(**data)
                db.session.add(pokemon)

        if i % 20 == 0:
            db.session.commit()
            print(f"{i} Pokémon traités...")

        time.sleep(0.5)

    db.session.commit()
    print("Tous les Pokémon importés avec succès !")