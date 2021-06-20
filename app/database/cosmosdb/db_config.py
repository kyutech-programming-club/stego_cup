import os

settings = {
  'host': os.environ.get('ACCOUNT_HOST', 'https://cosmos-kanashimi.documents.azure.com:443/'),
  'master_key': os.environ.get('ACCOUNT_KEY', 'DVD5MXX4AqUZilQZhnvheFVi2govWtPm0YUcBKzCKo81BsFNyphPqiKo58knTwyMAJTet17EgpGhL8j851E4eA=='),
  'database_id': os.environ.get('COSMOS_DATABASE', 'Stego-cup'),
  'container_id': os.environ.get('COSMOS_CONTAINER', 'Question'),
}
