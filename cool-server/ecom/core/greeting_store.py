import io
import uuid
from dataclasses import dataclass
from typing import Optional

import logging

import requests

from ecom.core import dynamodb_wrapper
from ecom.core import s3_wrapper

logger = logging.getLogger(__name__)


@dataclass
class GreetingItem:
    greeting_id: str
    topic: str
    greeting: str
    picture_download_link: str


def _download_picture_to_s3(url: str, picture_id: str):
    logger.info('url=%s, picture_id=%s', url, picture_id)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    content_type = resp.headers.get('content-type')
    assert content_type == 'image/jpeg', \
        RuntimeError(f'Unsupported content-type: {content_type}')
    with io.BytesIO(resp.content) as file_obj:
        s3_wrapper.put_file(f'{picture_id}.jpg', file_obj)


def add_greeting(topic: str, greeting: str, picture_url: str) -> str:
    logger.info(
        'topic=%s, greeting=%s, picture_url=%s', topic, greeting, picture_url)
    greeting_id = str(uuid.uuid4())
    _download_picture_to_s3(picture_url, greeting_id)
    dynamodb_wrapper.put_greeting(greeting_id, greeting, topic)
    return greeting_id


def get_greeting_by_id(greeting_id: str) -> Optional[GreetingItem]:
    logger.info('greeting_id=%s', greeting_id)
    greeting_data = dynamodb_wrapper.get_greeting_by_id(greeting_id)
    if greeting_data:
        greeting_data['picture_download_link'] = s3_wrapper.get_download_link(
            f'{greeting_id}.jpg')
        greeting_data['greeting_id'] = greeting_data.pop('id')
        return GreetingItem(**greeting_data)
    return None
