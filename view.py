from models import User
from app import app
from app import db


from flask import Flask, url_for, render_template, request, redirect, session


@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def home():
    session['logged_in'] = False
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        pw = request.form['password']
        try:
            user_login = User.query.filter_by(username=name, password=pw).first()
            if user_login:
                session['logged_in'] = True
                return render_template('index.html')
            else:
                return 'Ведены не верные данные...'
        except:
            return render_template('register.html') 
    else:
    	return render_template('register.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html') 


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))