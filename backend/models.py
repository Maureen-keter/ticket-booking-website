from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db=SQLAlchemy()

class User(db.Model, SerializerMixin):
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String)
    lastName=db.Column(db.String)
    email=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    role=db.Column(db.String, default="User")
    