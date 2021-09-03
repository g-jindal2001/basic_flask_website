from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import pymysql
from demo_website import python_secrets
from flask_bcrypt import Bcrypt

app = Flask(__name__)

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(python_secrets.dbuser, python_secrets.dbpass, python_secrets.dbhost, python_secrets.dbname)

#app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from demo_website import routes