from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    OMPs = db.relationship('OMP', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read password')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class OMP(db.Model):
    __tablename__ = 'omp'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    comments = db.relationship('Comment', backref = 'omp', lazy = 'dynamic')
    
    def __init__(self, title, content):
      self.title = title
      self.content = content
      
    def save_omp(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_omp(cls):
        omps = OMP.query.filter_by().all()
        return omps
        
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String)
    OMP_id = db.Column(db.Integer,db.ForeignKey('omp.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def __init__(self, message):
      self.message = message
      
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls):
        comments = Comment.query.filter_by().all()
        return comments
        
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    omp = db.relationship('OMP', backref = 'category', lazy = 'dynamic')
    
    def __repr__(self):
        return f'Category {self.name}'
    