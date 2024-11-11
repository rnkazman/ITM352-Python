# Quiz game example
from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)
@app.route("/")
def home():
    return(render_template('index.html'))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global QUESTIONS, question_num, score, question_list
    
    #Check if the user has answered a question
    if request.method == 'POST':
        return redirect(url_for('result'))
    
    # Load the question and options to display
    question_num += 1
    return render_template('quiz.html', num=question_num, question=question_list[question_num-1][0], 
                           options=question_list[question_num-1][1])  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)

question_file = open('questions.json')
QUESTIONS = json.load(question_file)
question_list = list(QUESTIONS.items())
question_num = 0
score = 0

# Run the application
if __name__ == '__main__':
    app.run(debug=True)