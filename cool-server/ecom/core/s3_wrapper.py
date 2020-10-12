from functools import lru_cache
from typing import BinaryIO

import boto3

from ecom import config


@lru_cache()
def _s3_client() -> object:
    return boto3.client(
        's3', endpoint_url=config.S3_ENDPOINT_URL,
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY)


def get_download_link(s3_key: str) -> str:
    return _s3_client().generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': config.GREETING_PICTURES_BUCKET_NAME,
            'Key': s3_key,
        },
        ExpiresIn=3600,
    )


def put_file(s3_key: str, file_obj: BinaryIO) -> None:
    _s3_client().upload_fileobj(
        file_obj,
        config.GREETING_PICTURES_BUCKET_NAME, s3_key,
        ExtraArgs={'ContentType': 'image/jpeg'})
