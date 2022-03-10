from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(uuid.uuid4())

db = SQLAlchemy(app)

import application.routes