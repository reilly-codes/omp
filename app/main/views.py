from flask import render_template,redirect,url_for
from . import main

@main.route('/')
def index():
    title = 'MAKE AN EXQUISITE IMPRESSION'
    
    return render_template('home.html', title = title)