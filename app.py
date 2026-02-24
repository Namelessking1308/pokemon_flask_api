from flask import Flask
from config import Config
from models import db

def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from routes.pokemon_routes import pokemon_bp
    app.register_blueprint(pokemon_bp)

    return app

app = creat_app()

if __name__ == "__main__":
    app.run(debug=True)