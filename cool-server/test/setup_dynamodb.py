import sys
import boto3

from ecom import config


TEST_GREETINGS = {
    '1': {
        'topic': 'Christmas',
        'greeting': 'Merry Christmas!',
    },
    '2': {
        'topic': 'Diwali',
        'greeting': 'Happy Diwali!',
    },
    '3': {
        'topic': 'Mid-Summer',
        'greeting': 'Hyvää Juhannusta!',
    },
}


def fix_naive_is_dst():
    import dateutil.tz
    import time

    def _fixed_naive_is_dst(self, dt):
        # pylint: disable=W0212
        timestamp = dateutil.tz.tz._datetime_to_timestamp(dt)
        if timestamp + time.timezone < 0:
            current_time = timestamp + time.timezone + 31536000
        else:
            current_time = timestamp + time.timezone
        return time.localtime(current_time).tm_isdst

    # pylint: disable=W0212
    dateutil.tz.tzlocal._naive_is_dst = _fixed_naive_is_dst


def delete_greetings_table():
    dynamo_db_client = boto3.client(
        'dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)

    table_names = dynamo_db_client.list_tables().get('TableNames')
    if config.GREETINGS_TABLE_NAME not in table_names:
        return

    print(f'Deleting table: {config.GREETINGS_TABLE_NAME}')
    dynamo_db_client.delete_table(TableName=config.GREETINGS_TABLE_NAME)


def create_greetings_table():
    dynamo_db_client = boto3.client(
        'dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)

    table_names = dynamo_db_client.list_tables().get('TableNames')
    if config.GREETINGS_TABLE_NAME in table_names:
        print(f'Table already exists: {config.GREETINGS_TABLE_NAME}')
        return

    print(f'Creating table: {config.GREETINGS_TABLE_NAME}')
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)

    table = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        TableName=config.GREETINGS_TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
    )

    table.wait_until_exists()


def populate_test_data():
    print(f'Populating table: {config.GREETINGS_TABLE_NAME}')
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)
    table = dynamodb.Table(config.GREETINGS_TABLE_NAME)

    with table.batch_writer() as batch:
        for id, greeting in TEST_GREETINGS.items():
            item = greeting
            item['id'] = id
            batch.put_item(Item=item)


def recreate_all():
    if sys.platform == 'win32':
        fix_naive_is_dst()
    delete_greetings_table()
    create_greetings_table()
    populate_test_data()


if __name__ == '__main__':
    recreate_all()
