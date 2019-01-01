import persistence.politico_neo as politicos
from flask_restful import Resource


class PoliticosAPI(Resource):
    """ PoliticosAPI """

    def get(self):
        politicos_data = politicos.get_politicos()
        if politicos_data:
            return politicos_data
        else:
            return {}, 404


