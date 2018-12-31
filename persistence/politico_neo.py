""" Politico persistence """

from persistence.db_neo import driver
from json import dumps

# QUERIES
DELETE_POLITICO_PARTIDO_RELATION = 'MATCH (p:Politico {uuid:{uuid}})-[r:PARTIDO]-() DELETE r'
UPDATE_POLITICO_PARTIDO = 'MATCH (p:Politico),(x:Partido) ' \
                           'WHERE p.uuid={uuid} AND x.partido={partido}' \
                           'MERGE (p)-[r:PARTIDO]->(x)' \
                           'ON CREATE SET p.partido=x.partido, p.partido_filtro=x.partido_filtro ' \
                           'RETURN p'
MATCH_POLITICO = 'MATCH (p:Politico {uuid:{uuid}}) RETURN PROPERTIES(p) AS `data`'
CREATE_POLITICO = 'CREATE (p:Politico {politico}) RETURN ID(p)'


def get_politico(uuid):

    with driver.session() as session:
        politico = session.run(MATCH_POLITICO, uuid=uuid)
        if politico:
            return dumps(politico.data())
        else:
            return None


def update_politico(uuid, partido):

    with driver.session() as session:
        # Delete previous relation
        session.run(DELETE_POLITICO_PARTIDO_RELATION, uuid=uuid)
        # Create new relation and updates properties partido and partido_filtro from related node.
        session.run(UPDATE_POLITICO_PARTIDO, uuid=uuid, partido=partido)
        #TODO: Si el partido no existe se queda huerfano de partido.


def create_politico(politico):

    with driver.session() as session:
        lal = session.run(CREATE_POLITICO, politico=politico)
        print(lal.data())


if __name__ == '__main__':
    politico = {
        "partido_filtro": "Otros partidos",
        "mensual": "3277,45",
        "institucion": "Ayuntamiento de Cartaya",
        "observa": "Dedicación Exclusiva",
        "nombre": "LOLO",
        "ccaa": "Andalucía",
        "sueldo_base": "45884,30",
        "genero": "Hombre",
        "anual": "45884,30",
        "cargo_filtro": "Alcalde",
        "cargo": "Alcalde",
        "dietas": "0,00",
        "partido": "ICAR"
    }
    create_politico(politico)
    #update_politico('78debc00-0c54-11e9-8ef9-a45e60c1370f', 'PP')
    #print(get_politico('78debc00-0c54-11e9-8ef9-a45e60c1370f'))

