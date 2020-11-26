#__init__.py under the slproject folder

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
#Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from slproject.sdwan.views import sdwan_blueprint
from slproject.sda.views import sda_blueprint

app.register_blueprint(sdwan_blueprint,url_prefix="/sdwan")
app.register_blueprint(sda_blueprint,url_prefix='/sda')