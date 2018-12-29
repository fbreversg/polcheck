from flask_restful import Resource


class PoliticosAPI(Resource):
    """ PoliticosAPI skeleton """

    def get(self):
        return {'PoliticosAPI': 'GET test OK'}

