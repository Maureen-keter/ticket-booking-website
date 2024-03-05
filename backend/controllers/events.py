from flask import make_response, jsonify, request
from flask_restful import Resource, abort
from models import Event, db
from datetime import datetime

class Events(Resource):
    def get(self):
        events=[event.to_dict() for event in Event.query.all()]
        return make_response(jsonify(events), 200)

    def post(self):
        data=request.get_json()
        date_str=data['date']
        start_time_str = data['start_time']
        date=datetime.strptime(date_str, '%Y-%m-%d')
        start_time = datetime.strptime(start_time_str, '%H:%M').time()

        new_event=Event(name=data['name'], location=data['location'],  max_attendees=data['max_attendees'], date=date, start_time=start_time)        
        db.session.add(new_event)
        db.session.commit()
        return make_response(jsonify({"message":"new event created successfully"}), 200)
    
class EventById(Resource):
    def get(self, id):
        event=Event.query.get(id).to_dict()
        return make_response(jsonify(event), 200)
    def patch(self, id):
        event = Event.query.get(id)
        if not event:
            abort(404, detail = f'Event with {id=} does not exist')
        data = request.get_json()
        for key, value in data.items():
            if value is None:
                continue
            if key=='start_time':
                value=datetime.strptime(value, '%H:%M').time()
            setattr(event, key, value)
        db.session.commit()
        return event.to_dict()
    def delete(self, id):
        event = Event.query.get(id)
        if not event:
            abort(404, detail = f'Event with {id=} does not exist')
        db.session.delete(event)
        db.session.commit()  