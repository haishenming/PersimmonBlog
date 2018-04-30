from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from app.art import art as art_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(art_blueprint, url_prefix="/art")
