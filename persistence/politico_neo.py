""" Politico persistence """

from persistence.db_neo import driver

# QUERIES
CREATE_POLITICO = ""


def create_politico():

    with driver.session() as session:
        results = session.run(CREATE_POLITICO)
        return True # TODO: Revisar tipos de retorno.


if __name__ == '__main__':
    # TODO: Tests.
    create_politico()
