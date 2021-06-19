from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app.database.cosmosdb.cosmos import *

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  problems = select_all_questions(container)
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem", methods=('GET', 'POST') )
def problem(id):
  problem_list = select_problem(container, id)
  temp_ans = problem_list[1]

  if request.method == 'POST':
    answer = select_ans(container, id)
    code = request.form['code']
    if code == "":
      code = temp_ans

    ans_list = answer.splitlines()
    code_list = code.splitlines()

    is_correct = 1

    if ans_list.length != code_list.length:
      is_correct = 0
    else:
      for ans_line, code_line in zip(ans_list, code_list):
        print(ans_line)
        print(code_line)
        if ans_line != code_line:
          is_correct = 0
          break

    return redirect(url_for('problems.result', is_correct=is_correct))

  problem = problem_list[0]
  choice_ans = select_choice_ans(container, id)

  return render_template( 'problem.html', 
                          problem=problem,
                          temp_ans=temp_ans,
                          choice_ans=choice_ans
                        )
@bp.route("/<int:is_correct>/result")
def result(is_correct):
  return render_template('result.html', is_correct=is_correct)

