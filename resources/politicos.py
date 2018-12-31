import persistence.politico_neo as politicos
from flask import jsonify
from flask_restful import Resource


class PoliticosAPI(Resource):
    """ PoliticosAPI """

    def get(self):
        return politicos.get_politicos()


