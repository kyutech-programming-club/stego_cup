from flask import Flask, Blueprint

bp = Blueprint('controllers', __name__)

@bp.route("/")
def hello():
    return "Hello, World!"

