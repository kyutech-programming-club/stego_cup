from flask import Flask, Blueprint, render_template
from app.database.cosmosdb.cosmos import *

bp = Blueprint('problems', __name__)

@bp.route("/")
def index():
  problems = select_all_questions(container)
  return render_template('index.html', problems=problems)
  
@bp.route("/<int:id>/promblem", methods=('GET', 'POST') )
def problem(id):
  if request.method == 'POST':
    answer = select_ans(container, id)
  
  problem_list = select_problem(container, id)
  problem = problem_list[0]
  temp_ans = problem_list[1]
  choice_ans = select_choice_ans(container, id)
  return render_template( 'problem.html', 
                          problem=problem,
                          temp_ans=temp_ans,
                          choice_ans=choice_ans
                        )

