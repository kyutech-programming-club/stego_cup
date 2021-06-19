from flask import Flask, Blueprint, render_template

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  problems = {1:"hoge1", 2:"hoge2"}
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem")
def problem(id):
  problems = {1:"hoge1", 2:"hoge2"}
  return render_template('problem.html', problem=problems[id])

