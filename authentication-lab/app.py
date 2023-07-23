from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyBFqU7fSxnYJ8TtN6PBrX0EOcEmOsLnZv0",
  "authDomain": "morrie-pyrebase.firebaseapp.com",
  "projectId": "morrie-pyrebase",
  "storageBucket": "morrie-pyrebase.appspot.com",
  "messagingSenderId": "635855264485",
  "appId": "1:635855264485:web:a6ccd5eca7ff98edc3520c",
  "measurementId": "G-YT44VY8PDS",
  "databaseURL": ""
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = 
                auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)