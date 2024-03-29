from flask import Flask, request, make_response, jsonify
from flask_bcrypt import Bcrypt
from flask_restful import Resource, Api, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import User, db

bcrypt = Bcrypt()
jwt = JWTManager()
class Users(Resource):
    def get(self):
        users=User.query.all()
        user_dict=[user.to_dict() for user in users]
        return make_response(jsonify(user_dict), 200)
    
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

    
    
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            abort(404, detail="User does not exist")
        if not bcrypt.check_password_hash(user.password, data['password']):
            abort(403, detail="Password is not correct")
        metadata = {"role": user.role}
        token = create_access_token(identity=user.email, additional_claims=metadata)
        return {"jwt-access-token": token}

class UserById(Resource):
    def get(self,id):
        users_list = []
        for user in User.query.filter_by(id=id):
            user_dict = {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "role": user.role,
                "email": user.email
            }
            users_list.append(user_dict)
        return make_response(jsonify(users_list), 200)
    
    def patch(self,id):
        user = User.query.get(id)
        if not user:
            abort(404, detail = f'User with {id=} does not exist')
        data = request.get_json()
        for key, value in data.items():
            if value is None:
                continue
            setattr(user, key, value)
        db.session.commit()
        return user.to_dict()
    
    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, detail = f'User with {id=} does not exist')        
        db.session.delete(user)
        db.session.commit()
        return {"detail": f"user with {id=} has been deleted successfully"}

class UserByToken(Resource):
    @jwt_required()
    def get(self):
        current_user_email = get_jwt_identity()
        print(current_user_email)
        current_user = User.query.filter_by(email=current_user_email).first()
        if not current_user:
            abort(404, detail="User not found")
        return make_response(jsonify(current_user.to_dict()), 200)