import os
from flask import Flask
from flask_cors import CORS


from ecom.service import (
    eservice,
)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(
    eservice.blueprint,
    url_prefix='/eservice')
