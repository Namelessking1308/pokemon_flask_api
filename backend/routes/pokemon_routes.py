from flask import Blueprint, jsonify
from models.pokemon import Pokemon
from services.pokeapi_service import fetch_pokemon_data
from models import db

pokemon_bp = Blueprint("pokemon", __name__)

@pokemon_bp.route("/pokemons", methods=["GET"])
def get_all_pokemons():
    pokemons = Pokemon.query.all()

    result = []
    for p in pokemons:
        result.append({
            "id": p.id,
            "name": p.name,
            "hp": p.hp,
            "attack": p.attack,
            "defense": p.defense,
            "sprite": p.sprite_url
        })

    return jsonify(result), 200

@pokemon_bp.route("/pokemon/import/<name>", methods=["POST"])
def import_pokemon(name):
    data = fetch_pokemon_data(name)

    if not data:
        return jsonify({"error": "Pokemon not found"}), 404

    existing = Pokemon.query.filter_by(name=data["name"]).first()
    if existing:
        return jsonify({"message": "Pokemon already exists"}), 400

    pokemon = Pokemon(**data)
    db.session.add(pokemon)
    db.session.commit()

    return jsonify({
        "message": "Pokemon imported successfully",
        "pokemon": {
            "id": pokemon.id,
            "name": pokemon.name
        }
    }), 201