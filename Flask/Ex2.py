from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    print("Hi there!")
#    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('success', username=username))
    else:
        return redirect(url_for('login'))


@app.route('/success/<username>')
def success(username):
    return f'Welcome, {username}!'


# Run the application
if __name__ == '__main__':
    app.run(debug=True)