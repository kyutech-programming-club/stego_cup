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

    if len(ans_list) != len(code_list):
      return redirect(url_for('problems.incorrect'))
    else:
      for ans_line, code_line in zip(ans_list, code_list):
        if ans_line != code_line:
          return redirect(url_for('problems.incorrect'))
          
    return redirect(url_for('problems.correct'))

  problem = problem_list[0]
  choice_ans = select_choice_ans(container, id)

  return render_template( 'problem.html', 
                          problem=problem,
                          temp_ans=temp_ans,
                          choice_ans=choice_ans,
                          id=id
                        )

@bp.route("/correct")
def correct():
  return render_template('correct.html')

@bp.route("/incorrect")
def incorrect():
  return render_template('incorrect.html')

