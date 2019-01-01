import persistence.politico_neo as politico_neo
from flask import request
from flask_restful import Resource, reqparse


class PoliticoAPI(Resource):
    """ PoliticoAPI """

    def put(self, id, partido):
        """ UPDATE politico"""
        return politico_neo.update_politico(id, partido)
        #TODO: Recuperar urls.

    def post(self):
        """ CREATE politico"""
        self.__politico_validate()
        return politico_neo.create_politico(request.get_json()), 201
        # TODO: Recuperar urls.

    # Improvement
    def get(self, id):
        """ GET politico"""
        politico_data = politico_neo.get_politico(id)
        if politico_data:
            return politico_data
        else:
            return {}, 404
        # TODO: Recuperar urls.

    # Improvement
    def delete(self, id):
        """ DELETE politico"""
        politico_neo.delete_politico(id)
        return {}, 204

    def  __politico_validate(self):
        """ Create form validation """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('nombre', required=True,
                            help="'nombre' cannot be blank!")
        parser.add_argument('mensual', required=True,
                            help="'mensual' cannot be blank!")
        parser.add_argument('institucion', required=True,
                            help="'institucion' cannot be blank!")
        parser.add_argument('observa', required=True,
                            help="'observa' cannot be blank!")
        parser.add_argument('ccaa', required=True,
                            help="'ccaa' cannot be blank!")
        parser.add_argument('sueldo_base', required=True,
                            help="'sueldo_base' cannot be blank!")
        parser.add_argument('genero', required=True,
                            help="'genero' cannot be blank!")
        parser.add_argument('anual', required=True,
                            help="'anual' cannot be blank!")
        parser.add_argument('cargo', required=True,
                            help="'cargo' cannot be blank!")
        parser.add_argument('dietas', required=True,
                            help="'dietas' cannot be blank!")
        parser.add_argument('partido', required=True,
                            help="'partido' cannot be blank!")

        parser.parse_args()
