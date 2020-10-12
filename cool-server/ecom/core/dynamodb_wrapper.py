from functools import lru_cache
from typing import List

import boto3

from ecom import config


@lru_cache()
def _greeting_table() -> object:
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)
    # pylint: disable=no-member
    return dynamodb.Table(config.GREETINGS_TABLE_NAME)


def get_greeting_ids() -> List[str]:
    return sorted([
        item.get('id')
        for item
        in _greeting_table().scan(ProjectionExpression='id').get('Items')
    ])


def get_greeting_by_id(greeting_id: str) -> dict:
    response = _greeting_table().get_item(
        Key={
            'id': greeting_id,
        }
    )
    return response.get('Item')


def put_greeting(greeting_id, greeting, topic):
    _greeting_table().put_item(Item={
        'id': greeting_id,
        'greeting': greeting,
        'topic': topic,
    })
