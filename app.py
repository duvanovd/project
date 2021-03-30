from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy


from flask_session  import  Session
from datetime import datetime, date
from flask_login import UserMixin

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
