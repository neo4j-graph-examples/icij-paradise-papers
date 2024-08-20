# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (a:Officer {name:$name})-[r:OFFICER_OF|INTERMEDIARY_OF|REGISTERED_ADDRESS*..10]-(b)
RETURN b.name as name LIMIT 20
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        name="Ross, Jr. - Wilbur Louis",
        database_="neo4j")
    for record in result.records:
        print(record['name'])
