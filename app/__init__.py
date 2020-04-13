import os
from flask import Flask, flash, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
app = Flask(__name__)
app.config.from_object(__name__)
UPLOAD_FOLDER = "./app/static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
app.config['SECRET_KEY'] = "$Private"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vubrzmtoyljnqs:bcb71b1d576cf7c7b3b1b43f776b8492868de164d0c1809d743233729129a092@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d8f6dbl75sgbaq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
