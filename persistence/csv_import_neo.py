""" CSV Import ETL """
from common.config import CSV_FILE
from persistence.db_neo import driver

CREATE_CARGO_NODE_QUERY = 'LOAD CSV WITH HEADERS FROM "file:///tmp/import.csv" AS row FIELDTERMINATOR ";"' \
                        'MERGE (:Cargo {cargo: row.CARGO, cargo_filtro: row.CARGO_PARA_FILTRO});'


CREATE_CCAA_NODE_QUERY = 'LOAD CSV WITH HEADERS FROM "file:///tmp/import.csv" AS row FIELDTERMINATOR ";"' \
                        'MERGE (:Ccaa {ccaa: row.CCAA});'


CREATE_GENERO_NODE_QUERY = 'LOAD CSV WITH HEADERS FROM "file:///tmp/import.csv" AS row FIELDTERMINATOR ";"' \
                        'MERGE (:Genero {genero: row.GENERO});'


CREATE_PARTIDO_NODE_QUERY = 'LOAD CSV WITH HEADERS FROM "file:///tmp/import.csv" AS row FIELDTERMINATOR ";"' \
                        'MERGE (:Partido {partido: row.PARTIDO, partido_filtro: row.PARTIDO_PARA_FILTRO});'


CREATE_POLITICO_NODE_QUERY = 'LOAD CSV WITH HEADERS FROM "file:///tmp/import.csv" AS row FIELDTERMINATOR ";"' \
                             'MATCH (g:Genero {genero:row.GENERO}), (c:Ccaa {ccaa:row.CCAA}), ' \
                             '(o:Cargo {cargo:row.CARGO}), (x:Partido {partido:row.PARTIDO, partido_filtro: row.PARTIDO_PARA_FILTRO})' \
                             'MERGE (p:Politico {nombre: row.TITULAR, partido: row.PARTIDO, ' \
                             'partido_filtro: row.PARTIDO_PARA_FILTRO,' \
                             'genero: row.GENERO, cargo: row.CARGO, cargo_filtro: row.CARGO_PARA_FILTRO,' \
                             'institucion: row.INSTITUCION, ccaa: row.CCAA})' \
                             'ON CREATE SET ' \
                             'p.sueldo_base=row.SUELDOBASE_SUELDO, p.mensual=row.RETRIBUCIONMENSUAL, ' \
                             'p.dietas=row.OTRASDIETASEINDEMNIZACIONES_SUELDO,' \
                             'p.anual=row.RETRIBUCIONANUAL, p.observa=row.OBSERVACIONES ' \
                             'MERGE (p)<-[rg:GENERO]-(g)' \
                             'MERGE (p)<-[rc:CCAA]-(c)' \
                             'MERGE (p)<-[ro:CARGO]-(o)' \
                             'MERGE (p)<-[rp:PARTIDO]-(x)'


def import_csv():

    # Comment dbms.directories.import=import for being able to get the csv from any folder.
    # A better aproach would be using neo4j tools for import but was mandatory to create a import endpoint.
    with driver.session() as session:

        # CARGO node creation
        session.run(CREATE_CARGO_NODE_QUERY, csvfile=CSV_FILE)

        # CCAA node creation
        session.run(CREATE_CCAA_NODE_QUERY, csvfile=CSV_FILE)

        # GENERO node creation
        session.run(CREATE_GENERO_NODE_QUERY, csvfile=CSV_FILE)

        # GENERO node creation
        session.run(CREATE_PARTIDO_NODE_QUERY, csvfile=CSV_FILE)

        # POLITICO node creation
        session.run(CREATE_POLITICO_NODE_QUERY, csvfile=CSV_FILE)


if __name__ == '__main__':
    import_csv()

