from flask import Flask, render_template, request, url_for, redirect
import random
import sympy as sp

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i in range(1, 11):
            answer = float(request.form[f'answer{i}'])
            if round(answer, 2) == round(float(request.form[f'correct{i}']), 2):
                score += 1
        return render_template('score.html', score=score)

    x = sp.Symbol('x')
    questions = []
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        x_value = random.randint(1, 10)
        c = a + b * x_value
        equation = a + b * x - c
        correct = sp.solve(equation, x)[0]
        questions.append((a, b, c, correct))

    return render_template('quiz.html', questions=questions)


@app.route('/score')
def score():
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True)
