""" Politico persistence """

from persistence.db_neo import driver

# QUERIES
DELETE_POLITICO_PARTIDO_RELATION = 'MATCH (p:Politico {uuid:{uuid}})-[r:PARTIDO]-() DELETE r'
UPDATE_POLITICO_PARTIDO = 'MATCH (p:Politico),(x:Partido) ' \
                          'WHERE p.uuid={uuid} AND x.partido={partido} ' \
                          'MERGE (p)<-[r:PARTIDO]-(x) ' \
                          'ON CREATE SET p.partido={partido}, p.partido_filtro=x.partido_filtro ' \
                          'RETURN PROPERTIES(p) AS `data`'
MATCH_POLITICO = 'MATCH (p:Politico {uuid:{uuid}}) RETURN PROPERTIES(p) AS `data`'
MATCH_POLITICO_WITHOUT_UUID = 'MATCH (p:Politico {nombre: {politico}.nombre, mensual: {politico}.mensual, ' \
                              'institucion: {politico}.institucion, observa: {politico}.observa, ' \
                              'ccaa: {politico}.ccaa, sueldo_base: {politico}.sueldo_base, genero: {politico}.genero, ' \
                              'anual: {politico}.anual, cargo: {politico}.cargo, dietas: {politico}.dietas, ' \
                              'partido: {politico}.partido}) ' \
                              'RETURN PROPERTIES(p) AS `data`'
CREATE_POLITICO = 'MATCH (x:Partido {partido:{politico}.partido}), (g:Genero {genero:{politico}.genero}),' \
                  '(c:Ccaa {ccaa:{politico}.ccaa}), (o:Cargo {cargo:{politico}.cargo}) ' \
                  'MERGE (p:Politico {nombre: {politico}.nombre, mensual: {politico}.mensual, ' \
                  'institucion: {politico}.institucion, observa: {politico}.observa, ccaa: {politico}.ccaa, ' \
                  'sueldo_base: {politico}.sueldo_base, genero: {politico}.genero, anual: {politico}.anual, ' \
                  'cargo: {politico}.cargo, dietas: {politico}.dietas, partido: {politico}.partido}) ' \
                  'MERGE (p)<-[rp:PARTIDO]-(x) ' \
                  'ON CREATE SET p.partido_filtro=x.partido_filtro ' \
                  'MERGE (p)<-[rg:GENERO]-(g) ' \
                  'MERGE (p)<-[rc:CCAA]-(c) ' \
                  'MERGE (p)<-[ro:CARGO]-(o) ' \
                  'ON CREATE SET p.cargo_filtro=o.cargo_filtro ' \
                  'RETURN PROPERTIES(p) AS `data`'
DELETE_POLITICO = 'MATCH (p:Politico {uuid:{uuid}}) DETACH DELETE p'
MATCH_POLITICOS = 'MATCH (p:Politico) RETURN PROPERTIES(p) AS `data` LIMIT 50'


def get_politico(uuid):

    with driver.session() as session:
        politico_record = session.run(MATCH_POLITICO, uuid=uuid).single()
        if politico_record:
            return politico_record.data()
        else:
            return None


def update_politico(uuid, partido):

    with driver.session() as session:
        # Delete previous relation
        session.run(DELETE_POLITICO_PARTIDO_RELATION, uuid=uuid)
        # Create new relation and updates property partido_filtro from related node.
        politico_record = session.run(UPDATE_POLITICO_PARTIDO, uuid=uuid, partido=partido).single()
        if politico_record:
            return politico_record.data()
        else:
            return None


def create_politico(politico):

    with driver.session() as session:
        politico_record = session.run(CREATE_POLITICO, politico=politico).single()
        if politico_record:
            # Little workaround to get the UUID since its creation is lazy and needs another operation after create.
            return session.run(MATCH_POLITICO_WITHOUT_UUID, politico=politico).single()
        else:
            return None


def delete_politico(uuid):

    with driver.session() as session:
        session.run(DELETE_POLITICO, uuid=uuid)


def get_politicos():

    with driver.session() as session:
        results = session.run(MATCH_POLITICOS)
        if results:
            return results.data()
        else:
            return None
