from flask import Flask, render_template, request, redirect, url_for
from string import ascii_lowercase
import random
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This will display a welcome message and a "Start Quiz" button

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global question_num, QUESTIONS, score # get access to the question_num variable outside the function

    # Check if the user has answered a question
    if request.method == 'POST':
        # Logic to capture the user’s answers 
        if(request.form.get('answer') == QUESTIONS[questions[question_num-1][0]][0]):
            # increment the score
            score += 1
            the_result = "🥳 Correct! 🥳"
        else:
            the_result = "🤔 Incorrect 🤔"
        # Display the result of the question
        return render_template('question_result.html', question_result = the_result, question = questions[question_num-1][0], answer = request.form.get('answer')) 
    
    # Display the next question
    question_num += 1 # increment the question counter
    # quiz over? then redirect to the result page
    if(question_num > len(questions)):
        return redirect(url_for('result'))
    # get the question and answer options
    a_question = questions[question_num-1][0]
    ordered_alternatives = random.sample(questions[question_num-1][1], k=len(questions[question_num-1][1]))

    return render_template('quiz.html', num=question_num, question= a_question, options=ordered_alternatives)  # Displays the question and options

@app.route('/result')
def result():
    global score, question_num # get access to the score and question_number variables outside the function
    # get the result template before resetting the score and question number
    template = render_template('result.html', score=score, total=len(questions))
    score = 0; # reset the score
    question_num = 0; # reset the question counter
    return template 


# Functions for main processing steps
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐\n")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}\n")
        return 0

# Main quiz steps: preparing questions, running the quiz, giving feedback
# Read in and load the file of quiz questions
f = open('questions.json')
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = json.load(f)
questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)

question_num = 0; # initialize the question counter
score = 0; # initialize the score

# Run the application
if __name__ == '__main__':
    app.run(debug=True)