import persistence.politico_neo as politico
from flask import jsonify
from flask_restful import Resource


class PoliticoAPI(Resource):
    """ PoliticoAPI skeleton """

    def put(self, id, partido):
        jsonify(politico.update_politico(id, partido))
        return '', 204
        #TODO: Recuperar urls.

    def post(self, id):
        return {'PoliticoAPI': 'POST test OK'}
        # TODO: Recuperar urls.

    # Improvement
    def get(self, id):
        return politico.get_politico(id)
        # TODO: Recuperar urls.

    # Improvement
    def delete(self, id):
        return {'PoliticoAPI': 'DELETE test OK'}
