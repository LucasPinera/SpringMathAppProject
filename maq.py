from flask import Flask, render_template, request, url_for, redirect
import random
import sympy as sp
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)


# Define the home route
@app.route('/')
def home():
    return render_template('home.html')


# Function to generate an easy question
def generate_easy_question():
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        x_value = random.randint(1, 10)
        c = a + b * x_value
        if b != 0:
            return a, b, c, x_value


# Function to generate a medium question
def generate_medium_question():
    while True:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        x_value = random.randint(-10, 10)
        c = a + b * x_value
        if b != 0:
            return a, b, c, x_value


# Function to generate a hard question
def generate_hard_question():
    while True:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        x_value = round(random.uniform(-10, 10), 1)

        # Create an equation with parentheses and more operations
        eq_value = a * (x_value + b) + c * (x_value - d)
        # Make sure there are not 0

        if a != 0 and b != 0 and c != 0 and d != 0 and eq_value.is_integer():
            return a, b, c, d, int(eq_value), x_value


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Handling form submission
    if request.method == 'POST':
        score = 0
        wrong_questions = []  # Store the questions the user got wrong

        i = 1
        while True:
            try:
                # Retrieve user and correct answers from the form
                user_answer_str = request.form.get(f'simple_answer{i}', None)
                correct_answer_str = request.form.get(f'simple_correct{i}', None)
                question_str = request.form.get(f'simple_question{i}', None)

                if user_answer_str is None or correct_answer_str is None or question_str is None:
                    user_answer_str = request.form.get(f'complex_answer{i}', None)
                    correct_answer_str = request.form.get(f'complex_correct{i}', None)
                    question_str = request.form.get(f'complex_question{i}', None)

                if user_answer_str is None or correct_answer_str is None or question_str is None:
                    break

                # Convert user and correct answers to float
                user_answer = float(user_answer_str) if user_answer_str else None
                correct_answer = float(correct_answer_str)

                # Compare answers and update score and wrong_questions list
                if user_answer is not None and round(user_answer, 2) == round(correct_answer, 2):
                    score += 1
                else:
                    question_parts = [float(x) for x in
                                      question_str.split(',')]  # I changed this line from int to float

                    if len(question_parts) == 3:  # Easy & Medium? question
                        a, b, c = question_parts
                        wrong_questions.append((a, b, c, correct_answer))
                    else:  # Hard question
                        a, b, c, d, eq_value = question_parts
                        wrong_questions.append((a, b, c, d, eq_value, correct_answer))

                i += 1
            except BadRequestKeyError:
                break

        # Render the score template with results
        return render_template('score.html', score=score, wrong_questions=wrong_questions)

    # Handle the quiz generation for different difficulties
    difficulty = request.args.get('difficulty', 'easy')

    simple_questions = []
    complex_questions = []

    # Generate easy questions
    while len(simple_questions) < 10 and difficulty == "easy":
        a, b, c, x_value = generate_easy_question()
        simple_questions.append((a, b, c, x_value))

    # Generate medium questions
    while len(simple_questions) < 10 and difficulty == "medium":
        a, b, c, x_value = generate_medium_question()
        simple_questions.append((a, b, c, x_value))

    # Generate hard questions
    while len(complex_questions) < 10 and difficulty == "hard":
        a, b, c, d, eq_value, x_value = generate_hard_question()
        complex_questions.append((a, b, c, d, eq_value, x_value))

    # Render the quiz template with the generated questions
    return render_template('quiz.html', simple_questions=simple_questions, complex_questions=complex_questions)


@app.route('/score')
def score():
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True)
