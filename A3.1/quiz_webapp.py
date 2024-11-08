# Quiz game example
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/")
def home():
    return(render_template('index.html'))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global QUESTIONS
    
    #Check if the user has answered a question
    if request.method == 'POST':
        return redirect(url_for('result'))
    
    # Load the question and options to display
    return render_template('quiz.html')  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)