from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    satisfaction = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    # q3 = db.Column(db.Text)
    # q4 = db.Column(db.Text)
    # q5 = db.Column(db.Text)
    # q6 = db.Column(db.Text)

    def __init__(self, age, income, satisfaction, q1, q2):
        self.age = age
        self.income = income
        self.satisfaction = satisfaction
        self.q1 = q1
        self.q2 = q2
        # self.q3 = q3
        # self.q4 = q4
        # self.q5 = q5
        # self.q6 = q6

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    satisfaction = []
    q1 = []
    q2 = []
    # q3 = []
    # q4 = []
    # q5 = []
    # q6 = []

    for el in fd_list:
        satisfaction.append(int(el.satisfaction))
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        # q3.append(int(el.q3))
        # q4.append(int(el.q4))
        # q5.append(int(el.q5))
        # q6.append(int(el.q6))

    if len(satisfaction) > 0:
        mean_satisfaction = statistics.mean(satisfaction)
    else:
        mean_satisfaction = 0

    if len(q1) > 0:
        mean_q1 = statistics.mean(q1)
    else:
        mean_q1 = 0

    if len(q2) > 0:
        mean_q2 = statistics.mean(q2)
    else:
        mean_q2 = 0
    #
    # if len(q3) > 0:
    #     mean_q3 = statistics.mean(q3)
    # else:
    #     mean_q3 = 0
    #
    # if len(q4) > 0:
    #     mean_q4 = statistics.mean(q4)
    # else:
    #     mean_q4 = 0
    #
    # if len(q5) > 0:
    #     mean_q5 = statistics.mean(q5)
    # else:
    #     mean_q5 = 0
    #
    # if len(q6) > 0:
    #     mean_q6 = statistics.mean(q6)
    # else:
    #     mean_q6 = 0

    # Prepare data for google charts
    data = [['Satisfaction', mean_satisfaction], ['Future work', mean_q1], ['Influence', mean_q2]]

    return render_template('result.html', data=data)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    age = request.form['age']
    income = request.form['income']
    satisfaction = request.form['satisfaction']
    q1 = request.form['q1']
    q2 = request.form['q2']
    #  q3 = request.form['q3']
    # q4 = request.form['q4']
    # q5 = request.form['q5']
    # q6 = request.form['q6']

    # Save the data
    fd = Formdata(age, income, satisfaction, q1, q2)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
