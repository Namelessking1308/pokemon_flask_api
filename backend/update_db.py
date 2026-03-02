from app import app
from models import db, Pokemon, Combat

with app.app_context():
    db.create_all()
    
    pokemons = Pokemon.query.all()
    for p in pokemons:
        p.sprite_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p.id}.png'
        db.session.add(p)
    db.session.commit()
    print("Sprite URLs mises à jour !")