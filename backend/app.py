from flask import Flask, make_response, jsonify
from controllers.users import Users, UserById, UserByToken, UserLogin
from controllers.events import Events, EventById
from controllers.tickets import Tickets, TicketById
from models import db
from flask_migrate import Migrate
from flask_restful import Resource, Api
from dotenv import load_dotenv
load_dotenv()






app=Flask(__name__)

app.config.from_prefixed_env()

migrate=Migrate(app, db)
db.init_app(app)

api=Api(app)



class Home(Resource):
    def get(self):
        response_dict={
            "Message":"Ticket booking API"
        }
        response=make_response(
            response_dict,
        )
        return make_response(jsonify(response), 200)
      






api.add_resource(Home, '/')
api.add_resource(Users,'/users')
api.add_resource(UserLogin,'/login')
api.add_resource(UserById,'/users/<int:id>')
api.add_resource(UserByToken,'/user-token')
api.add_resource(Events,'/events')
api.add_resource(EventById, '/events/<int:id>')
api.add_resource(Tickets, '/tickets')
api.add_resource(TicketById, '/tickets/<int:id>')

if __name__=='__main__':
    app.run(port=5555, debug=True)
