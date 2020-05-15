from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from Users import Users
from UserById import UserById


db_connect = create_engine('sqlite:///exemplo.db')
app = Flask(__name__)
api = Api(app)
api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<id>') 

if __name__ == '__main__':
    app.run()