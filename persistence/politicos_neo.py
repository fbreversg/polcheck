""" Politicos persistence """

from persistence.db_neo import driver
from persistence.db_queries import GET_POLITICOS


def get_politicos():

    with driver.session() as session:
        results = session.run(GET_POLITICOS)
        for result in results:
            print(result.data('id'))
            print(result.data('properties'))


if __name__ == '__main__':
    get_politicos()
