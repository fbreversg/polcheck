import os
from neo4j import GraphDatabase

db_user = os.getenv("NEO4J_USER")
db_pass = os.getenv("NEO4J_PASSWORD")
db_uri = os.getenv("NEO4J_URI")

driver = GraphDatabase.driver(db_uri, auth=(db_user, db_pass))

with driver.session() as session:
    results = session.run("MATCH p=()-[r:PARTIDO]->() RETURN p LIMIT 25")
    for result in results:
        print(result)
