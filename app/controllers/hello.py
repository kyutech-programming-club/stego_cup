from flask import Flask, Blueprint

bp = Blueprint('hello', __name__)

@bp.route("/")
def hello():
    return "Hello, World!"

