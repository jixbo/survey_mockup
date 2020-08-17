from flask import Flask, request
import json
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
from model import db, Question, Dependency, generate_questions

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.sqlite3'

db.init_app(app)

with app.app_context():
    db.create_all()
    n = Question.query.order_by(desc("id")).first().id


#Api will return answer 4 after answer two, dependency answer for question 3 is not fulfilled but for 4 is
#curl http://localhost:5000/api/question/ -d '{"id":2,"answer":"no"}' -X POST -H "Content-Type: application/json"
#curl http://localhost:5000/api/question/ -d '{"id":3,"answer":"yes"}' -X POST -H "Content-Type: application/json"
#curl http://localhost:5000/api/question/ -d '{"id":4,"answer":"yes"}' -X POST -H "Content-Type: application/json"

answers = {}

@app.route('/', methods=['GET'])
def answer():
    return "<h1>Survey</h1><p>We need to ask you a few things</p>"
    

@app.route('/api/question/', methods=['POST'])
def survey():
    print (n)

    current = request.get_json().get("id")
    answers[current] = request.get_json().get("answer")


    next = current + 1
    q = Question.query.get(next)
    while next <= n:
        deps = Dependency.query.filter_by(question_id_dependant=next)
        depend_fulfilled = True
        count = deps.count()
        if deps.count() > 0:
            for d in deps:
                #Dependenden answer does not exist or does not match
                if not (d.question_id_answer in answers and answers[d.question_id_answer] == d.answer):
                    depend_fulfilled = False
                    break

        if depend_fulfilled is True:
            response = app.response_class(
                response = json.dumps({"question":q.text, "answers":q.answers, "id":next}),
                status = 200,
                mimetype = 'application/json'
            )
            return response
        else:
            next += 1

    else:
        response = app.response_class(
            response = json.dumps({"question":"no more questions", "id":-1}),
            status = 201,
            mimetype = 'application/json'
        )
        return response


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)