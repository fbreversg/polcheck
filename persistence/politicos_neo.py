""" Politicos persistence """

from persistence.db_neo import driver


def get_politicos():

    with driver.session() as session:
        results = session.run("MATCH (n:Politico) RETURN n LIMIT 25")
        for result in results:
            print(result)


if __name__ == '__main__':
    get_politicos()
