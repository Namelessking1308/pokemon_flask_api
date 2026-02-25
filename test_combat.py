from app import app
from models import db, Pokemon, Combat
from services.battle_engine import BattleEngine  # ton moteur de combat

def run_test_combat(pokemon1_id, pokemon2_id):
    with app.app_context():
        # Récupérer les Pokémon depuis la DB
        p1 = Pokemon.query.get(pokemon1_id)
        p2 = Pokemon.query.get(pokemon2_id)

        if not p1 or not p2:
            print("Un des Pokémon n'existe pas !")
            return

        # Lancer le combat via le BattleEngine
        battle = BattleEngine(p1, p2)
        winner, turns, logs = battle.fight()  # <- tuple unpacking

        # Enregistrer le combat dans la DB
        combat_record = Combat(
            pokemon1_id=p1.id,
            pokemon2_id=p2.id,
            winner_id=winner.id,
            turns=turns,
            battle_log=logs
        )
        db.session.add(combat_record)
        db.session.commit()

        print(f"Combat terminé : {p1.name} vs {p2.name}")
        print(f"Gagnant : {winner.name} en {turns} tours")
        print("Logs du combat :")
        for log in logs:
            print(log)

if __name__ == "__main__":
    # Test automatique avec les deux premiers Pokémon de ta DB
    run_test_combat(1, 2)