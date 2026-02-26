from flask import Blueprint, request, jsonify
from models import db
from models.pokemon import Pokemon
from models.combat import Combat
from services.battle_engine import BattleEngine

combat_bp = Blueprint("combat_bp", __name__)

@combat_bp.route("/combat", methods=["POST"])
def combat():
    data = request.get_json()
    p1 = Pokemon.query.get(data.get("pokemon1_id"))
    p2 = Pokemon.query.get(data.get("pokemon2_id"))

    if not p1 or not p2:
        return jsonify({"error": "Pokémon introuvable"}), 404

    engine = BattleEngine(p1, p2)
    winner, turns, logs = engine.fight()

    new_combat = Combat(
        pokemon1_id=p1.id,
        pokemon2_id=p2.id,
        winner_id=winner.id,
        turns=turns,
        battle_log=logs
    )

    db.session.add(new_combat)
    db.session.commit()

    return jsonify({
        "winner": winner.name,
        "turns": turns,
        "logs": logs
    })