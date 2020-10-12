import os

import boto3

from ecom import config


def create_bucket():
    s3 = boto3.client(
        's3', endpoint_url=config.S3_ENDPOINT_URL,
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY)

    bucket_names = [
        bucket.get('Name')
        for bucket
        in s3.list_buckets().get('Buckets')
    ]

    if config.GREETING_PICTURES_BUCKET_NAME not in bucket_names:
        print(f'Creating bucket: {config.GREETING_PICTURES_BUCKET_NAME}')
        s3.create_bucket(Bucket=config.GREETING_PICTURES_BUCKET_NAME,
                         CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})


def populate_files():
    s3 = boto3.client(
        's3', endpoint_url=config.S3_ENDPOINT_URL,
        aws_access_key_id=config.S3_ACCESS_KEY,
        aws_secret_access_key=config.S3_SECRET_KEY)

    pictures_dir = os.path.join(os.path.dirname(__file__), 'pictures')

    TEST_DATA = [
        (1, 'christmas.jpg'),
        (2, 'diwali.jpg'),
        (3, 'juhannus.jpg'),
    ]

    for picture_id, file_name in TEST_DATA:
        s3.upload_file(
            os.path.join(pictures_dir, file_name),
            config.GREETING_PICTURES_BUCKET_NAME, f'{picture_id}.jpg',
            ExtraArgs={'ContentType': 'image/jpeg'}
        )


if __name__ == '__main__':
    create_bucket()
    populate_files()
