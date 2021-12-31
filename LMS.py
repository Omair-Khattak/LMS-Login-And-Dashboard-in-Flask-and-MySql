from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

  
  
app = Flask(__name__)
  
  
app.secret_key = 'omair khattak'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'lab'
  
mysql = MySQL(app)
  
@app.route('/', methods =['POST', 'GET'])
def index():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM student WHERE username = %s AND password = %s', (username, password))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['firstname'] = account[1]
            session['username'] = account[4]
            msg = 'Logged in successfully !'
            return redirect(url_for('dashboard'))
        else:
            msg = 'Incorrect username / password !'
        
    return render_template('login.html', msg = msg)
  
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/grades')
def grades():
    return render_template('grades.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')
