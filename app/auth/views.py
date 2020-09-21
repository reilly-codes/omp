from flask import render_template,redirect,url_for
from . import auth

@auth.route('/')
def index():
    title = 'MAKE AN EXQUISITE IMPRESSION'
    
    return render_template('auth/login.html', title = title)