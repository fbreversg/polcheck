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
api.add_resource(CSVImportAPI, '/import', '/polcheck/import', endpoint='import')
api.add_resource(PoliticosAPI, '/index', '/polcheck/politicos', endpoint='politicos')
api.add_resource(PoliticoAPI, '/update/<id>', methods=['PUT'], endpoint='update')
api.add_resource(PoliticoAPI, '/create/<id>', methods=['POST'], endpoint='create')
api.add_resource(PoliticoAPI, '/polcheck/politicos/<id>', endpoint='politico')


if __name__ == '__main__':
    app.run(debug=True)
