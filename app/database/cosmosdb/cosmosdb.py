import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

import DB_config

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Cosmos account -
#    https:#azure.microsoft.com/en-us/documentation/articles/documentdb-create-account/
#
# 2. Microsoft Azure Cosmos PyPi package -
#    https://pypi.python.org/pypi/azure-cosmos/
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic CRUD operations on a Item resource for Azure Cosmos
# ----------------------------------------------------------------------------------------------------------

HOST = DB_config.settings['host']
MASTER_KEY = DB_config.settings['master_key']
DATABASE_ID = DB_config.settings['database_id']
CONTAINER_ID = DB_config.settings['container_id']

def run_sample():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )

    db = client.get_database_client(DATABASE_ID)
    container = db.get_container_client(CONTAINER_ID)

    query = "SELECT q.question FROM Question q WHERE q.id = '2'"
    items = container.query_items(query, enable_cross_partition_query=True)
    print(' --- read_query --- ')
    print(list(items))

if __name__ == '__main__':
    run_sample()
