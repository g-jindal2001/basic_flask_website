from flask import render_template, url_for, redirect
from flask_login import  login_user, login_required, logout_user

from demo_website import app, db, bcrypt
from demo_website.models import User
from demo_website.forms import LoginForm, RegisterForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm() #Creating an instance of our LoginForm

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)#Log in the user
                return redirect(url_for('dashboard'))

    return render_template('login.html', form = form)# passing it down to our html template

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form = form)