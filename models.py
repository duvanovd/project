from app import db
from datetime import datetime, date
from flask_login import UserMixin
import re



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


    def __repr__(self):
        return '<User %r>' % self.username