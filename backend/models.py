from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re
from sqlalchemy import Time

db=SQLAlchemy()

class User(db.Model,SerializerMixin):
    serialize_rules=('-created_events', '-tickets',)
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50), default='USER')

    created_events=db.relationship('Event', backref='user')
    tickets=db.relationship('Ticket', backref='user')

    @validates('role')
    def validate_role(self, key, role):
        valid_roles = {'ADMIN', 'TECH-WRITER', 'USER'}
        normalized_role = role.upper()  
        if role.upper() not in valid_roles:
            raise ValueError("Role must be 'ADMIN', 'TECH-WRITER' or 'USER'")
        return normalized_role
    
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email
    

    
class Event(db.Model, SerializerMixin):
    serialize_rules=( '-tickets',)
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time= db.Column(db.Time, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    max_attendees = db.Column(db.Integer, nullable=False)

    creator_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    tickets=db.relationship("Ticket", backref="event")

class Ticket(db.Model, SerializerMixin):
    __tablename__='tickets'
    id=db.Column(db.Integer, primary_key=True)
    ticket_type=db.Column(db.String, nullable=False)
    reserved_by=db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id=db.Column(db.Integer, db.ForeignKey('events.id'))
    price=db.Column(db.Integer, nullable=False)

    @validates('ticket_type')
    def validate_tickets(self, key, ticket_type):
        valid_tickets=['VIP', 'REGULAR']
        normalized_tickets=ticket_type.upper()
        if normalized_tickets not in valid_tickets:
            raise ValueError("Ticket must either be 'VIP' or 'REGULAR'")
        return normalized_tickets

  


    