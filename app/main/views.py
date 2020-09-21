from flask import render_template,redirect,url_for,request,abort
from . import main

@main.route('/')
def index():
    title = 'MAKE AN EXQUISITE IMPRESSION'
    
    return render_template('home.html', title = title)

@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title = 'Profile'
    
    return render_template('profile/profile.html', title = title)