""" Flask server """
from flask import Flask
from flask_restful import Api
from resources.politico import PoliticoAPI
from resources.politicos import PoliticosAPI
from resources.csv_import import CSVImportAPI

# Flask singleton
app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(PoliticoAPI, '/create', '/update''/polcheck/politicos/<id>', endpoint='politico')
api.add_resource(PoliticosAPI, '/index', '/polcheck/politicos', endpoint='politicos')
api.add_resource(CSVImportAPI, '/import', endpoint='import')
