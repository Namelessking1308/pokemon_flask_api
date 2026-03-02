from flask import Blueprint, request, jsonify
from models import Pokemon
import random

combat_bp = Blueprint("combat_bp", __name__)

@combat_bp.route("/battle", methods=["POST"])
def battle():

    data = request.json

    p1 = Pokemon.query.get(data["pokemon1_id"])
    p2 = Pokemon.query.get(data["pokemon2_id"])

    if not p1 or not p2:
        return jsonify({"error": "Pokemon not found"}), 404

    hp1 = p1.hp
    hp2 = p2.hp
    turns = 0
    logs = []

    attacker_turn = True

    while hp1 > 0 and hp2 > 0:
        turns += 1

        if attacker_turn:
            damage = max(1, p1.attack - p2.defense // 2)
            hp2 -= damage

            logs.append({
                "attacker": p1.name,
                "defender": p2.name,
                "damage": damage,
                "hp1": max(hp1, 0),
                "hp2": max(hp2, 0)
            })

        else:
            damage = max(1, p2.attack - p1.defense // 2)
            hp1 -= damage

            logs.append({
                "attacker": p2.name,
                "defender": p1.name,
                "damage": damage,
                "hp1": max(hp1, 0),
                "hp2": max(hp2, 0)
            })

        attacker_turn = not attacker_turn

    winner = p1.name if hp1 > 0 else p2.name

    return jsonify({
        "winner": winner,
        "turns": turns,
        "logs": logs,
        "hp1": max(hp1, 0),
        "hp2": max(hp2, 0)
    })