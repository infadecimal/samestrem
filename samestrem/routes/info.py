from flask import Blueprint, jsonify, request
from os import chmod
from app import app

info = Blueprint('info', __name__)

@info.route("/info/")
def keys_index():
    return jsonify(message="You hit the INFO index")

