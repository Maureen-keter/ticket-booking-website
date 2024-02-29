from flask import Flask, make_response, jsonify, request
from models import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Resource, Api, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

bcrypt = Bcrypt()
jwt = JWTManager()


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa-daily.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


class User(Resource):
    def get():
        users=[user.to_dict for user in User.query.all()]
        return make_response(jsonify(users), 200)
    def post(self):
        data = request.get_json()
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            abort(409, detail="User Already Exists")
        if data['password'] == data['confirm-password']:
            hashed_password = bcrypt.generate_password_hash(data['password'])
            # Check if role is provided, otherwise default to "user"
            role = data.get('role', 'user')
            new_user = User(firstname=data['firstname'], lastname=data['lastname'], email=data['email'], password=hashed_password, role=role)
            db.session.add(new_user)
            db.session.commit()
            return make_response(jsonify(new_user.to_dict()), 201)
        else:
            abort(403, detail="Password and Confirm Password do not match")








api.add_resource(Home, '/')
api.add_resource(User, 'users')
api.add_resource(UserById, 'users/<int:id>')

if __name__=='__main__':
    app.run(debug=True)
