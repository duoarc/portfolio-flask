#! /usr/bin/env python3
import os
from flask import Flask, render_template, redirect, request, flash, jsonify
import locale
from flask.helpers import url_for
from flask_mail import Mail, Message

# from werkzeug.utils import redirect

app = Flask(__name__)

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, ContactForm

engine = create_engine('sqlite:///resume.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)


@app.route('/', methods = ['GET','POST'])
def resumeContact():
    if request.method == "POST":
        
        newMessage = ContactForm(name = request.form['contactName'], email = request.form['contactEmail'], subject = request.form['contactSubject'], message = request.form['contactMessage'])
        msg = Message(request.form['contactSubject'], sender = request.form['contactEmail'], recipients = ['abdmuhammad610@gmail.com'])
        msg.body = request.form['contactMessage']
        #mail.send(msg)
        session.add(newMessage)
        session.commit()

        flash ("Your message was sent, thank you!")
        return render_template('index.html', )
    else:  
        return render_template ('index.html')





if __name__ == '__main__':
    app.secret_key = "super_secret_keeey"
    app.debug = True
    app.run()