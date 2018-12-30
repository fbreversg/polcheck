""" Politicos persistence """

from persistence.db_neo import driver

# QUERIES
GET_POLITICOS = "MATCH (n:Politico) RETURN PROPERTIES(n) AS `data` LIMIT 50"


def get_politicos():

    with driver.session() as session:
        results = session.run(GET_POLITICOS)
        for record in results.records():
            return record.data()


if __name__ == '__main__':
    # TODO: Tests.
    get_politicos()
