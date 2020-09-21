from flask_mail import Message
from flask import render_template
from app import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'ryanner534@gmail.com'
    
    email = Message(syubject,sender = sender_email,recipients=[to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    mail.send(email)