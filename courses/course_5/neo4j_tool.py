from neo4j import GraphDatabase

from courses.config.neo4j_credentials import get_neo4j_password


def run_cypher_query(query: str):
    uri = "neo4j://localhost:7687"
    username = "neo4j"
    password = get_neo4j_password()

    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        records, summary, keys = driver.execute_query(query, database_="aicourse")
        for record in records:
            print(record.data())

        return [record.data() for record in records]
