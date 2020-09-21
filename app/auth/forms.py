from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required(),Email()])
    username = StringField('Your Desired Username' validators = [Required()])
    password = PasswordField('Password', validators = [Required(), EqualTo('password_confirm', message = 'Passwords do not match!')])
    password_confirm = PasswordField('Confirm Password', validators = [Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field).first():
            raise ValidationError('There is an account with this email address')
        
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field).first():
            raise ValidationError('That username is already taken')
        
class LoginForm(FlaskForm):
    email = StringField('Your email address', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    submit = SubmitField('Sign In')