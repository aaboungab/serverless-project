import logging
import requests
import azure.functions as func
import random
from azure.cosmos import exceptions, CosmosClient, PartitionKey


def main(req: func.HttpRequest) -> func.HttpResponse:
                                        
    logging.info('Python HTTP trigger function processed a request.')

    nostring = requests.get('https://serverlesapp.azurewebsites.net/api/Service2?code=3eSiLVqdbhfFevajXg44gTvoOhYpvWw5osjEnX7/IbdXL6tlNE9rfg==')

    letterstring = requests.get('https://serverlesapp.azurewebsites.net/api/Service3?code=Cb8B1BGrrM2xFXjFqKF64hYsbOuj2/gzQycKMsqtMgsfjQ6caT/Fqg==')

    combined = nostring.text + letterstring.text
    logging.info(nostring.text)
    logging.info(letterstring.text)

    endpoint = 'https://username-app.documents.azure.com:443/'
    key = 'dow1z1e44lYvwSwdwLbrEWf8A2jloXV1zlKb0BQJbnDRkuqQzI13o1aflZma3Jf9Ry7Co2QTEXe8GRNE3HvZGg=='
    client = CosmosClient(endpoint, key)
    database_name = "username-app"
    database = client.create_database_if_not_exists(id=database_name)

    container_name = "usercontainer"
    container = database.create_container_if_not_exists(
                                        id=container_name,
                                        partition_key=PartitionKey(path="/username"),
                                        offer_throughput=400
                                             )
    
    item_to_add = {
            "id": str(random.randint(0,100)),
            "username": combined
                  }
    
    container.create_item(body=item_to_add)

    return func.HttpResponse(
             combined,
             status_code=200
             )
