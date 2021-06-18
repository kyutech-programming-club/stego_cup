from flask import Flask, Blueprint, render_template

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  return render_template('index.html')
  
@bp.route("/promblem")
def problem(id):
  return render_template('problem.html')

