# test_combat.py
from app import app
from models import db
from models.pokemon import Pokemon
from models.combat import Combat
from services.battle_engine import BattleEngine

def run_test_combat(p1, p2):
    """Effectue un combat entre deux objets Pokémon"""
    with app.app_context():
        battle = BattleEngine(p1, p2)
        winner, turns, logs = battle.fight()

        # Enregistrement dans la DB
        combat_record = Combat(
            pokemon1_id=p1.id,
            pokemon2_id=p2.id,
            winner_id=winner.id,
            turns=turns,
            battle_log=logs
        )
        db.session.add(combat_record)
        db.session.commit()

        # Affichage des résultats
        print(f"\nCombat terminé : {p1.name} vs {p2.name}")
        print(f"Gagnant : {winner.name} en {turns} tours")
        print("Logs du combat :")
        for log in logs:
            print(log)

def get_pokemon():
    """Demande à l'utilisateur de choisir un Pokémon par nom ou ID"""
    choice_type = input("Voulez-vous choisir par 'id' ou par 'nom' ? ").strip().lower()
    with app.app_context():
        if choice_type == "id":
            id1 = int(input("ID du premier Pokémon : "))
            id2 = int(input("ID du second Pokémon : "))
            p1 = Pokemon.query.get(id1)
            p2 = Pokemon.query.get(id2)
        elif choice_type == "nom":
            name1 = input("Nom du premier Pokémon : ").strip().lower()
            name2 = input("Nom du second Pokémon : ").strip().lower()
            p1 = Pokemon.query.filter_by(name=name1).first()
            p2 = Pokemon.query.filter_by(name=name2).first()
        else:
            print("Choix invalide !")
            return None, None
    return p1, p2

if __name__ == "__main__":
    p1, p2 = get_pokemon()
    if p1 and p2:
        run_test_combat(p1, p2)
    else:
        print("Combat annulé : Pokémon introuvable.")