from flask import render_template,redirect,url_for,request,abort
from . import main
from ..models import User,OMP,Comment
from .forms import OMPForm
from app import db

@main.route('/')
def index():
    title = 'MAKE AN EXQUISITE IMPRESSION'
    omps = OMP.query.all()
    
    return render_template('home.html', title = title, omps = omps)

@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title = 'Profile'
    
    return render_template('profile/profile.html', title = title)

@main.route('/new/omp', methods = ['GET', 'POST'])
def new_omp():
    form = OMPForm()
    if form.validate_on_submit():
        title = form.title.data
        omp = form.description.data
        new_omp = OMP(title = title, content = omp)
        db.session.add(new_omp)
        db.session.commit()
        
        return redirect(url_for('.index'))
    
    title = 'New OMP'
    return render_template('new_omp.html', title = title, omp_form = form)

@main.route('/opm/<int:id>')
def opm(line_id):
    Pickup = OMP.query.filter_by(opm.id == line_id).first()
    if Pickup is None:
        abort(404)
    
    return render_template('full_opm.html', pickup = Pickup)