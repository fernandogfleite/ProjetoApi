from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


db_connect = create_engine('sqlite:///exemplo.db')

class Users(Resource):
    
    
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        if "name" in request.json.keys() and "email" in request.json.keys(): 
            name = request.json['name']
            email = request.json['email']

            conn.execute(
                "insert into user values(null, '{0}','{1}')".format(name, email))

            query = conn.execute('select * from user order by id desc limit 1')
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)
        return Response("nome e email são campos requeridos", status = 400)
            

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']

        conn.execute("update user set name ='" + str(name) +
                     "', email ='" + str(email) + "'  where id =%d " % int(id))

        query = conn.execute("select * from user where id=%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)