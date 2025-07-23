# Placeholder for app.py
from flask import Flask, render_template, redirect, request, session, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure secret key
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        session['user'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', username=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
