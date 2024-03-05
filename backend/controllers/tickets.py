from flask import make_response, jsonify, abort, request
from flask_restful import Resource, abort
from models import Ticket, db

class Tickets(Resource):
    def get(self):
        events=[ticket.to_dict() for ticket in Ticket.query.all()]
        return make_response(jsonify(events), 200)
    
    def post(self):
        data=request.get_json()
        new_ticket=Ticket(ticket_type=data['ticket_type'], reserved_by=data['user_id'], event_id=data['event_id'], price=data['price'])
        db.session.add(new_ticket)
        db.session.commit()
        return make_response(jsonify({"message":"new event created successfully"}), 200)
    

class TicketById(Resource):
    def get(self, id):
        ticket=Ticket.query.get(id).to_dict()
        return make_response(jsonify(ticket), 200)    
    
    def patch(self, id):
        ticket = Ticket.query.get(id)
        if not ticket:
            abort(404, detail = f'Ticket with {id=} does not exist')
        data = request.get_json()
        for key, value in data.items():
            if value is None:
                continue
            setattr(ticket, key, value)
        db.session.commit()
        return ticket.to_dict()
    def delete(self, id):
        ticket= Ticket.query.get(id)
        if not ticket:
            abort(404, detail = f'Ticket with {id=} does not exist')
        db.session.delete()
        db.session.commit()  
