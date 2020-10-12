from flask import Blueprint, jsonify, request, abort
from flask_cors import cross_origin

from ecom.core import dynamodb_wrapper
from ecom.core import greeting_store

blueprint = Blueprint(__name__, __name__)


@cross_origin
@blueprint.route('/', methods=['GET'])
def get_greeting_ids():
    return jsonify(dynamodb_wrapper.get_greeting_ids())
