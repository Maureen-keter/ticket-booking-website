from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re

db=SQLAlchemy()

class User(db.Model, SerializerMixin):
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String)
    lastName=db.Column(db.String)
    email=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    role=db.Column(db.String, default="USER")

    @validates('role')
    def validate_role(self, key, role):
        valid_roles={"ADMIN", "USER"}
        normalized_role=role.upper()
        if role.upper not in valid_roles:
            raise ValueError("Role must be 'ADMIN or 'USER'")
        return normalized_role
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email
    
class Event(db.Model, SerializerMixin):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String())
    max_attendees=(db.Integer)
  


    