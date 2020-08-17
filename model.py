from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(100), nullable = False)
    answers = db.Column(db.String(100))
    def __init__(self, id, text):
        self.id = id
        self.text = text

class Dependency(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    answer = db.Column(db.String(100))
    question_id_dependant = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)
    question_id_answer = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)


def generate_questions():
    """     objects = [
        Question(1,"Where do you live?"),
        Question(2,"Are you currently using any cream?"),
        Question(3,"How much do you currently spend on creams each month?"),
        Question(4,"How much are you willing to spend on creams each month?"),
        Question(5,"Please describe your current skin issues")
    ]
    db.session.builk_save_objects(objects)
    db.session.commit() """
    q = Question(7,'How old are you?')
    db.session.add(q)
    db.session.commit()