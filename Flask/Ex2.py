# Create and process a simple login page 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        userid = request.form.get('username')
        userpass = request.form.get('password')

        # Check the username and password.  If successful take the user to a success page.
        if USERS.get(userid) == userpass:
            return redirect(url_for('success', username=userid))
        else:
            return("Sorry Charlie")
    else:
        return render_template('login.html')


@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)


USERS = {"port": "port123", 
         "kazman": "kazman123"}

# Run the application in debug mode.
if __name__ == '__main__':
    app.run(debug=True)    
