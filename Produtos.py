from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


db_connect = create_engine('sqlite:///produtos.db')

class Produtos(Resource):
    
    
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from produtos")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        if "nomeProduto" in request.json.keys() and "valorProduto" in request.json.keys() and "quantidadeProduto" in request.json.keys(): 
            nomeProduto = request.json['nomeProduto']
            valorProduto = request.json['valorProduto']
            quantidadeProduto = request.json['quantidadeProduto']

            conn.execute(f"insert into produtos values(null, '{nomeProduto}','{valorProduto}', {quantidadeProduto})")

            query = conn.execute('select * from produtos order by id desc limit 1')
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
            return jsonify(result)
        return Response("nomeProduto, valorProduto, quantidadeProduto são campos requeridos", status = 400)
            

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        nomeProduto = request.json['nomProduto']
        valorProduto = request.json['valProduto']
        quantidadeProduto = request.json['qtdProduto']

        conn.execute(f"update produtos set nomProduto = {str(nomeProduto)}, valProduto = {float(valorProduto)}, qtdProduto = {int(quantidadeProduto)}  where id ={int(id)} ")

        query = conn.execute(f"select * from user where id= {int(id)}")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)