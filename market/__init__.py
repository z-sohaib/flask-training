from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# app.config['SECRET_KEY'] = '4b0c0a1a46a9468e69e54d9d'
from market import routes
