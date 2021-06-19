from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app.database.cosmosdb.cosmos import *

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  problems = select_all_questions(container)
  print("problems is")
  print(problems)
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem", methods=('GET', 'POST') )
def problem(id):
  if request.method == 'POST':
    answer = select_ans(container, id)
    code = request.form['code']

    print("answer")
    print(answer)
    print("code")
    print(code)

    if answer == code:
      is_correct = 1
    else:
      is_correct = 0

    return redirect(url_for('problems.result', is_correct=is_correct))


  problem_list = select_problem(container, id)
  problem = problem_list[0]
  temp_ans = problem_list[1]
  choice_ans = select_choice_ans(container, id)
  return render_template( 'problem.html', 
                          problem=problem,
                          temp_ans=temp_ans,
                          choice_ans=choice_ans
                        )
@bp.route("/<int:is_correct>/result")
def result(is_correct):
  return render_template('result.html', is_correct=is_correct)

