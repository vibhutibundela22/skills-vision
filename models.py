from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    score = db.Column(db.Integer, default=0)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.PickleType, nullable=False)
    correct = db.Column(db.String(100), nullable=False)
