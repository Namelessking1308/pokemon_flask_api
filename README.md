# Full Stack Pokémon

Une application **Full Stack Pokémon** combinant :  

- **Backend** : Flask + SQLAlchemy + PostgreSQL  
- **Frontend** : Angular + TypeScript  

Le projet permet de :  
- Importer tous les Pokémon depuis [PokeAPI](https://pokeapi.co/) dans une base PostgreSQL  
- Afficher la liste des Pokémon avec leurs stats et images  
- Simuler des combats entre Pokémon depuis une interface Angular  
- Visualiser l’historique des combats  

---

## 🛠️ Structure du projet

```text
pokemon_api/
│
├── backend/                 # Code backend Flask
│   ├── app.py               # Point d’entrée Flask
│   ├── config.py            # Configuration DB et environnement
│   ├── models/              # Modèles SQLAlchemy
│   │   ├─ __init__.py       # db = SQLAlchemy()
│   │   ├─ pokemon.py
│   │   └─ combat.py
│   ├── routes/              # Endpoints Flask
│   │   ├─ __init__.py  
│   │   ├─ pokemon_routes.py
│   │   └─ combat_routes.py
│   ├── services/            # Logique métier
│   │   ├─ __init__.py  
│   │   ├─ battle_engine.py
│   │   └─ pokeapi_service.py
│   ├── import_all_pokemon.py # Import Pokémon depuis PokeAPI
│   ├── create_db.py          # Création DB et tables
│   ├── update_db.py          # Mise à jour DB (ex: sprite_url)
│   └── test_combat.py        # Test des combats
│
├── frontend/                # Code frontend Angular
│   ├── src/
│   │   ├── app/
│   │   │   ├── pages/
│   │   │   │   ├── pokemons/
│   │   │   │   ├── battle/
│   │   │   │   └── history/
│   │   │   └── components/
│   │   │       ├── pokemon-card/
│   │   │       └── battle-log/
│   │   └── ...
│   ├── package.json
│   └── angular.json
│
├── .gitignore              # Fichiers à ignorer
└── README.md               # Ce fichier