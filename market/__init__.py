import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '0339f475c8af0fa86a7a6bc0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes