import os

S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')

DYNAMODB_ENDPOINT_URL = os.getenv('DYNAMODB_ENDPOINT_URL')

GREETINGS_TABLE_NAME = os.getenv('GREETINGS_TABLE_NAME', 'GreetingsTable')
GREETING_PICTURES_BUCKET_NAME = os.getenv(
    'GREETING_PICTURES_BUCKET_NAME', 'greeting-pictures-kefkqo7pbsqcfrhgrrrj')
