from flask import Flask, render_template, request, url_for, redirect
import random
import sympy as sp

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

def generate_easy_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x_value = random.randint(1, 10)
    c = a + b * x_value
    return a, b, c

def generate_hard_question():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    x_value = random.uniform(-10, 10)
    c = round(a + b * x_value, 2)
    return a, b, c

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i in range(1, 11):
            user_answer_str = request.form[f'answer{i}']
            user_answer = float(user_answer_str) if user_answer_str else None

            if user_answer is not None and round(user_answer, 2) == round(float(request.form[f'correct{i}']), 2):
                score += 1

        return render_template('score.html', score=score)
    difficulty = request.args.get('difficulty', 'easy')

    x = sp.Symbol('x')
    questions = []
    for _ in range(10):
#        a = random.randint(1, 10)
#        b = random.randint(1, 10)
#        x_value = random.randint(1, 10)

        if difficulty == "hard":
            a, b, x_value = generate_hard_question()
        else:
            a, b, x_value = generate_easy_question()

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
