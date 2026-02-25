# Pokémon Flask API

Une API Flask pour récupérer et stocker les Pokémon depuis l'API officielle [PokeAPI](https://pokeapi.co/).

Ce projet est un mini-projet Python/Flask/PostgreSQL visant à :  
- Importer tous les Pokémon dans une base PostgreSQL  
- Stocker les informations principales (HP, attaque, défense, sprites, etc.)  
- Fournir une API REST avec Flask pour récupérer un Pokémon par nom, obtenir la liste complète ou simuler des combats  
- Permettre l’utilisation de Postman ou de tout client HTTP pour tester les endpoints  
- Préparer un frontend Angular pour interagir avec l’API

---

## Fonctionnalités actuelles

1. **Importation Pokémon** ✅
   - Récupération automatique depuis l’API PokeAPI
   - Stockage dans la base PostgreSQL
   - Endpoint pour récupérer tous les Pokémon ou un Pokémon par nom

2. **Simulation de combats** ⚡
   - Endpoint `/combat` pour simuler un combat entre deux Pokémon
   - Calcul des dégâts basé sur HP, attaque et défense
   - Retour du gagnant, du nombre de tours et d’un log détaillé tour par tour
   - Stockage automatique des combats dans la table `combats`

3. **API Flask** 🔹
   - Endpoint pour récupérer un Pokémon par nom :  
     ```
     GET /pokemon/<name>
     ```
   - Endpoint pour récupérer tous les Pokémon :  
     ```
     GET /pokemons
     ```
   - Endpoint pour simuler un combat :  
     ```
     POST /combat
     Body JSON: { "pokemon1_id": 1, "pokemon2_id": 2 }
     ```
   - Retour JSON : gagnant, tours, logs détaillés

---

## Fonctionnalités prévues / à venir

- **Historique des combats** 📜  
  - Endpoint pour récupérer tous les combats passés :  
    ```
    GET /combat/all
    ```
  - Permettra de lister tous les combats et leurs logs pour consultation ou statistiques

- **Amélioration du système de combat** ⚔️  
  - Prise en compte des types d’éléments pour appliquer des multiplicateurs de dégâts  
  - Ajout de nouvelles colonnes dans la table `pokemons` si besoin (ex : vitesse, capacité spéciale)  
  - Optimisation du BattleEngine pour des combats plus réalistes et cohérents avec l’univers Pokémon

- **Frontend Angular** 🌐  
  - Sélection de deux Pokémon depuis l’interface  
  - Affichage du combat en temps réel avec les logs et le gagnant  
  - Historique des combats consultable depuis l’interface  

---

## Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/NameLessKing1308/pokemon-flask-api.git
cd pokemon-flask-api

├─ app.py                # point d’entrée Flask
├─ config.py             # configuration de la base (sécurisée via .env)
├─ models/               # modèles SQLAlchemy
│   ├─ __init__.py       # db = SQLAlchemy()
│   ├─ pokemon.py
│   └─ combat.py
├─ routes/               # endpoints Flask
│   ├─ __init__.py  
│   ├─ pokemon_routes.py
│   └─ combat_routes.py
├─ services/             # logique métier
│   ├─ __init__.py  
│   ├─ battle_engine.py
│   └─ pokeapi_service.py
├─ import_all_pokemon.py # script pour importer les Pokémon depuis l’API
├─ create_db.py          # script pour créer la DB et les tables
├─ test_combat           # fichier pour tester les combats
├─ update_db            # fichier pour mettre à jour la DB
├─ requirements.txt      # dépendances Python
├─ README.md             # ce fichier
├─ .env                  # fichier local avec secrets (non versionné)
├─ .gitignore            # fichiers ignorés