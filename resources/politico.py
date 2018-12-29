from flask_restful import Resource


class PoliticoAPI(Resource):
    """ PoliticoAPI skeleton """

    def put(self, id):
        return {'PoliticoAPI': 'PUT test OK'}

    def post(self, id):
        return {'PoliticoAPI': 'POST test OK'}

    # Improvement
    def get(self, id):
        return {'PoliticoAPI': 'GET test OK'}

    # Improvement
    def delete(self, id):
        return {'PoliticoAPI': 'DELETE test OK'}
