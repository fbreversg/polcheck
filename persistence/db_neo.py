""" BD setup """

import os
from json import dumps


db_user = os.getenv("NEO4J_USER")
db_pass = os.getenv("NEO4J_PASSWORD")
db_uri = os.getenv("NEO4J_URI")

driver = GraphDatabase.driver(db_uri, auth=(db_user, db_pass))


def get_politicos():
    politicos = Politico.match(graph).limit(50)
    returnObject = []
    for politico in politicos:
        print(politico.cargo.get(0,0))


if __name__ == '__main__':
    # TODO: Tests.
    print(get_politicos())
    print(dumps(get_politicos()))
