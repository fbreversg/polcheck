""" Flask server """
from flask import Flask
from flask import got_request_exception
from flask_restful import Api

# Resources
from resources.politico import PoliticoAPI
from resources.politicos import PoliticosAPI
from resources.csv_import import CSVImportAPI

# Config
from common.api_errors import API_ERRORS
from common.config import MAX_UPLOAD_SIZE

# Flask singleton
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_SIZE
api = Api(app, catch_all_404s=True, errors=API_ERRORS)


# Routes
api.add_resource(CSVImportAPI, '/import', '/polcheck/import', endpoint='import')
api.add_resource(PoliticosAPI, '/index', '/polcheck/politicos', endpoint='politicos')
api.add_resource(PoliticoAPI, '/update/<id>', methods=['PUT'], endpoint='update')
api.add_resource(PoliticoAPI, '/create/<id>', methods=['POST'], endpoint='create')
api.add_resource(PoliticoAPI, '/polcheck/politicos/<id>', endpoint='politico')


if __name__ == '__main__':
    app.run(debug=True)
