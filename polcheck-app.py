""" Flask server """
from flask import Flask
from flask_restful import Api

# Resources
from resources.politico import PoliticoAPI
from resources.politicos import PoliticosAPI
from resources.csv_import import CSVImportAPI

# Config
from common.config import MAX_UPLOAD_SIZE

# Flask singleton
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_SIZE
api = Api(app)


# Routes
api.add_resource(CSVImportAPI, '/import', '/polcheck/import', endpoint='import')
api.add_resource(PoliticosAPI, '/index', '/polcheck/politicos', endpoint='politicos')
api.add_resource(PoliticoAPI, '/update/<id>/partidos/<partido>', '/polcheck/politicos/<id>/partidos/<partido>', methods=['PUT'], endpoint='update')
api.add_resource(PoliticoAPI, '/create/<id>', methods=['POST'], endpoint='create')
api.add_resource(PoliticoAPI, '/polcheck/politicos/<id>', endpoint='politico')


if __name__ == '__main__':
    app.run(debug=True)
