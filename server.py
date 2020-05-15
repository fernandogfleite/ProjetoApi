from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from json import dumps
from Produtos import Produtos
from ProdutosById import ProdutosById


app = Flask(__name__)
api = Api(app)
api.add_resource(Produtos, '/produtos')
api.add_resource(ProdutosById, '/produtos/<id>') 

if __name__ == '__main__':
    app.run()