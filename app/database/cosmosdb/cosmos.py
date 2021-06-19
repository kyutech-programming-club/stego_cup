import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import os
from app.database.cosmosdb.db_config import settings

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Cosmos account -
#    https:#azure.microsoft.com/en-us/documentation/articles/documentdb-create-account/
#
# 2. Microsoft Azure Cosmos PyPi package -
#    https://pypi.python.org/pypi/azure-cosmos/
# ----------------------------------------------------------------------------------------------------------

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
CONTAINER_ID = settings['container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})
db = client.get_database_client(DATABASE_ID)
container = db.get_container_client(CONTAINER_ID)

def select_question_all(container):
  try:
    query = "SELECT c.question FROM c"
    item = container.query_items(query, enable_cross_partition_query=True)
    question = list(item)
    return question[0]

  except exceptions.CosmosResourceNotFoundError:
    print('A database with id \'{0}\' does not exist'.format(id))

def select_question(container, id):
  try:
    query = "SELECT c.question FROM c WHERE c.id = \"{0}\"".format(id)
    item = container.query_items(query, enable_cross_partition_query=True)
    question = list(item)
    return question[0]['question']

  except exceptions.CosmosResourceNotFoundError:
    print('A database with id \'{0}\' does not exist'.format(id))

def ans_sentence(container, id):
  try:
    query = "SELECT c.answer FROM c WHERE c.id = \"{0}\"".format(id)
    item = container.query_items(query, enable_cross_partition_query=True)
    answer = list(item)
    return answer[0]['answer']

  except exceptions.CosmosResourceNotFoundError:
    print('A database with id \'{0}\' does not exist'.format(id))

def temp_ans(container, id):
  try:
    query = "SELECT c.temp_ans FROM c WHERE c.id = \"{0}\"".format(id)
    item = container.query_items(query, enable_cross_partition_query=True)
    answer = list(item)
    return answer[0]['temp_ans']

  except exceptions.CosmosResourceNotFoundError:
    print('A database with id \'{0}\' does not exist'.format(id))

def select_ans(container, id):
  try:
    query = "SELECT c.select_ans FROM c WHERE c.id = \"{0}\"".format(id)
    item = container.query_items(query, enable_cross_partition_query=True)
    answer = list(item)
    return answer[0]['select_ans']

  except exceptions.CosmosResourceNotFoundError:
    print('A database with id \'{0}\' does not exist'.format(id))

