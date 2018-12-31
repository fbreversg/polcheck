""" Politicos persistence """
"""
from persistence.db_neo import driver
from json import dumps

# QUERIES
GET_POLITICOS = "MATCH (n:Politico) RETURN PROPERTIES(n) AS `data` LIMIT 50"


def get_politicos():

    with driver.session() as session:
        results = session.run(GET_POLITICOS)
        if results:
            return dumps(results.data())
        else:
            return None


if __name__ == '__main__':
    # TODO: Tests.
    print(get_politicos())
"""
