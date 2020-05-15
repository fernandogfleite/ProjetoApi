from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///produtos.db')

class ProdutosById(Resource):
    
    def delete(self, id):
        conn = db_connect.connect()
        conn.execute(f"delete from produtos where id= {int(id)} ")
        return {"status": "success"}

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute(f"select * from produtos where id = {int(id)} ")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)