from flask import Flask, flash, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(__name__)
UPLOAD_FOLDER = "./app/static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
app.config['SECRET_KEY'] = "$Private"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yyjsiqipposnbx:0219e535e2e6f2559c94a3ddc266e8da9d75875b8cb23ee4b09177af7f2c0158@ec2-3-211-48-92.compute-1.amazonaws.com:5432/deohdgmcvl07nt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
