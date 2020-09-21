from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm, RegistrationForm
from app import db
from ..models import User
from ..email import mail_message

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid Email or Password')
     
    title = 'MAKE AN EXQUISITE IMPRESSION'
    
    return render_template('auth/login.html', title = title, login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('main.index'))

@auth.route('/', methods = ['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to OMP", "email/welcome_user", user.email, user = user)
        
        return redirect(url_for('auth.login'))
    
    title = 'MAKE AN EXQUISITE IMPERESSION'
    
    return render_template('auth/signup.html', title = title, registration_form = form)