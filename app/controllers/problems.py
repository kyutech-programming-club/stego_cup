from flask import Flask, Blueprint, render_template
from app.database.cosmosdb.cosmos import *

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  problems = {1:"hoge1", 2:"hoge2"}
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem")
def problem(id):
  problem = select_question_all(container)

  return render_template('problem.html', problem=problem)

