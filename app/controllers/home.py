from flask import Flask, Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route("/")
def index():
  return render_template('index.html')
  
