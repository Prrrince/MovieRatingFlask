#!/usr/bin/env python3
from flask import Flask, url_for
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
# from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '74854d3118b04499d4a1571f653ba889'

admin = Admin(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
Scss(app, static_dir='static', asset_dir='assets')

from movierating.admin import add_to_admin
add_to_admin()

from movierating import routes
