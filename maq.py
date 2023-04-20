from flask import Flask, render_template, request, url_for
import random
import sympy as sp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def math_quiz():
    score = None
    if request.method == 'POST':
        score = 0
        for i in range(1, 11):
            answer = float(request.form[f'answer{i}'])
            if round(answer, 2) == round(float(request.form[f'correct{i}']), 2):
                score += 1

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

    return render_template('index.html', questions=questions, score=score)



if __name__ == '__main__':
    app.run(debug=True)
