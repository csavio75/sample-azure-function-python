from azure.cosmos import exceptions, CosmosClient, ContainerProxy

def collection(container) -> ContainerProxy:
    url = "https://localhost:8081"
    key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
    
    client = CosmosClient(url, key, connection_verify=False)
    database_name = "SampleDB"

    try:
        database = client.create_database(id=database_name)
    except exceptions.CosmosResourceExistsError:
        database = client.get_database_client(database=database_name)

    return database.get_container_client(container)
