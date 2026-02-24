# Pokémon Flask API

Une API Flask pour récupérer et stocker les Pokémon depuis l'API officielle [PokeAPI](https://pokeapi.co/).

Ce projet est un mini-projet Python/Flask/PostgreSQL visant à :  
- Importer tous les Pokémon dans une base PostgreSQL  
- Stocker les informations principales (HP, attaque, défense, sprites, etc.)  
- Fournir une API REST avec Flask pour récupérer un Pokémon par nom ou obtenir la liste complète  
- Permettre l’utilisation de Postman ou de tout client HTTP pour tester les endpoints  

## Fonctionnalités

1. **Importation Pokémon** ✅
   - Récupération automatique depuis l’API PokeAPI
   - Stockage dans la base PostgreSQL

2. **Simulation de combats** ⚡
   - Permet de simuler des combats entre Pokémon (à implémenter)

3. **Historique des combats** 📜
   - Stocke les résultats des combats dans la base (à implémenter)

4. **API Flask** 🔹
   - Endpoint pour récupérer un Pokémon par nom :  
     ```
     GET /pokemon/<name>
     ```
   - Endpoint pour récupérer tous les Pokémon :  
     ```
     GET /pokemons
     ```

## Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/NameLessKing1308/pokemon-flask-api.git
cd pokemon-flask-api

Créer un environnement virtuel

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

Installer les dépendances

pip install -r requirements.txt

Créer le fichier .env à la racine avec ta connexion PostgreSQL

DATABASE_URL=postgresql://ton_user:ton_mdp@localhost:5433/ta_db

Créer la base de données et les tables

python create_db.py

Importer tous les Pokémon dans la base

python import_all_pokemon.py

Lancer le serveur Flask

python app.py

Le serveur tourne sur http://127.0.0.1:5000

2. **Utilisation**

Tester les endpoints avec Postman ou navigateur

Exemple pour récupérer Pikachu :

GET http://127.0.0.1:5000/pokemon/pikachu

Exemple pour récupérer tous les Pokémon :

GET http://127.0.0.1:5000/pokemons
Structure du projet
pokemon-flask-api/
├─ app.py               # point d’entrée Flask
├─ config.py            # configuration de la base (sécurisée via .env)
├─ models/              # modèles SQLAlchemy
│   └─ pokemon.py
├─ routes/              # endpoints Flask
│   └─ pokemon_routes.py
├─ import_all_pokemon.py # script pour importer les Pokémon depuis l’API
├─ create_db.py         # script pour créer la base et les tables
├─ requirements.txt     # dépendances Python
├─ README.md            # ce fichier
├─ .env                 # fichier local avec secrets (non versionné)
├─ .gitignore           # fichiers ignorés pour Git
Notes importantes

config.py et .env ne sont pas versionnés pour protéger les informations sensibles

Tous les scripts sont pensés pour fonctionner localement avec PostgreSQL

Pour GitHub, le dépôt contient uniquement le code et le README, sans mot de passe