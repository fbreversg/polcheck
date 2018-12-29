""" Flask server """
from flask import Flask
from flask import got_request_exception
from flask_restful import Api

# Resources
from resources.politico import PoliticoAPI
from resources.politicos import PoliticosAPI
from resources.csv_import import CSVImportAPI

# Config
import common.api_errors

# Flask singleton
app = Flask(__name__)
api = Api(app, catch_all_404s=True, errors=common.api_errors)


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.debug('Got exception during processing: %s', exception)


got_request_exception.connect(log_exception, app)

# Routes
api.add_resource(CSVImportAPI, '/import', '/polcheck/import', endpoint='import')
api.add_resource(PoliticosAPI, '/index', '/polcheck/politicos', endpoint='politicos')
api.add_resource(PoliticoAPI, '/update/<id>', methods=['PUT'], endpoint='update')
api.add_resource(PoliticoAPI, '/create/<id>', methods=['POST'], endpoint='create')
api.add_resource(PoliticoAPI, '/polcheck/politicos/<id>', endpoint='politico')


if __name__ == '__main__':
    app.run(debug=True)
