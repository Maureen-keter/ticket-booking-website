from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re

db=SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__="users"
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
    __tablename__='events'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String())
    max_attendees=(db.Integer)
    date=db.Column(db.DateTime)

class Ticket(db.Model, SerializerMixin):
    __tablename__='tickets'
    id=db.Column(db.Integer, primary_key=True)
    ticket_type=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id=db.Column(db.Integer, db.ForeignKey('events.id'))

    @validates('ticket_type')
    def validate_tickets(self, key, ticket_type):
        valid_tickets=['VIP', 'REGULAR']
        normalized_tickets=ticket_type.upper
        if ticket_type.upper not in valid_tickets:
            raise ValueError("Ticket must either be 'VIP' or 'REGULAR'")
        return normalized_tickets

  


    