#!/usr/bin/env bash
set -e
export PYTHONPATH=.

if [[ -z "${S3_ENDPOINT_URL}" ]]; then
    export S3_ENDPOINT_URL=http://localhost:19801
fi

if [[ -z "${DYNAMODB_ENDPOINT_URL}" ]]; then
    export DYNAMODB_ENDPOINT_URL=http://localhost:19802
fi

echo S3_ENDPOINT_URL: $S3_ENDPOINT_URL
echo DYNAMODB_ENDPOINT_URL: $DYNAMODB_ENDPOINT_URL

export S3_ACCESS_KEY=minio
export S3_SECRET_KEY=password
docker-compose up -d
python test/setup_s3.py
python test/setup_dynamodb.py

export PUBLIC_KEY='{ "kty": "RSA", "e": "AQAB","use": "sig","kid": "kate1","alg": "RS256","n": "mkHHLUCaM_mNRhuCW03vZLuwwNjhbEPVcusRD4ke3rWZjCPr8tqe05BzG4WPIT-jBzckY_we--X0VfNQ35DvrIUGgXWomCRTGxPGQTQBlf0RZfUinxMIXkgDRqRTdL3aGLJsq0qQc3OSkVGxJ1MEGGPe13cxMA9FmjdYgc35CFVQs02C4xpxeb6KpRS26OI06vhXEBWqaFhW9NhcZOIjUXBRo0O446KR08SJQtfb48IozkJm43i0TXArs-ZRjTsds-YjaHff-Z3E7HwLj9DGauC83vj67C-CUltZ_P1g_WTq7MQy_6gp0hFBSjdocE2DPhXBgPgw6-Bs5FbodfsUYw"}'

export FLASK_ENV=development
export FLASK_APP=ecom.service.app:app
flask run --host=0.0.0.0
