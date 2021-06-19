import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cosmos-kanashimi.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'foQIfGtOZGIvOTa0RdaFDw6cpmKHR0StWjdI4b9XDSR9cZcSVWTNoK9GnXmH1UQli2dyIWJvYOGDkhF7uBy12Q=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'Stego-cup'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Question'),
}
