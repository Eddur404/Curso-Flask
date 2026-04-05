from flask import Flask
from app.db import db
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '123456' 

db.init_app(app)
migrate = Migrate(app, db)


from app.controllers import default

