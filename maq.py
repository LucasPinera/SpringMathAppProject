from flask import Flask, render_template, request, url_for, redirect
import random
import sympy as sp

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


def generate_easy_question():
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        x_value = random.randint(1, 10)
        c = a + b * x_value
        if b != 0:
            return a, b, c, x_value

def generate_hard_question():
    while True:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        x_value = round(random.uniform(-10, 10), 1)
        c = a + b * x_value
        if b != 0 and c.is_integer():
            return a, b, int(c), x_value


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        wrong_questions = []  # Store the questions the user got wrong

        for i in range(1, 11):
            user_answer_str = request.form[f'answer{i}']
            user_answer = float(user_answer_str) if user_answer_str else None
            correct_answer = float(request.form[f'correct{i}'])

            if user_answer is not None and round(user_answer, 2) == round(correct_answer, 2):
                score += 1
            else:
                a, b, c = [int(x) for x in request.form[f'question{i}'].split(',')]
                wrong_questions.append((a, b, c, correct_answer))

        return render_template('score.html', score=score, wrong_questions=wrong_questions)
    difficulty = request.args.get('difficulty', 'easy')

    x = sp.Symbol('x')
    questions = []
    while len(questions) < 10:
        if difficulty == "hard":
            a, b, c, x_value = generate_hard_question()
        else:
            a, b, c, x_value = generate_easy_question()

        correct = x_value
        questions.append((a, b, c, correct))

    return render_template('quiz.html', questions=questions)


@app.route('/score')
def score():
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True)
