from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .pokemon import Pokemon
from .combat import Combat