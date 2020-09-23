from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from app import db


class OMPForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    description = TextAreaField('OMP Description')
    submit = SubmitField('Submit')