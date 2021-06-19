from flask import Flask, Blueprint, render_template, request

bp = Blueprint('problems', __name__)
app = Flask(__name__)

@bp.route("/")
def index():
  problems = {1:"hoge1", 2:"hoge2"}
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem", methods=['GET', 'POST'])
def problem(id):
  if request.method == 'POST':
    code = request.form['code']
  problems = {1:"hoge1", 2:"hoge2"}
  return render_template('problem.html', problem=problems[id])

