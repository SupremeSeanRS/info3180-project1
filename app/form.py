from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired , Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ProfileForm(FlaskForm):
    Fname = StringField('First Name', validators=[DataRequired()], id="inpFname")
    Lname = StringField('Last Name', validators=[DataRequired()], id="inpLname")
    Gender = SelectField('Gender', choices=[('S','Select Gender'),('Male', 'Male'), ('Female', 'Female')], id="gender")
    Email = StringField('Email', validators=[DataRequired(), Email()], id="inpEmail", render_kw={"placeholder": "e.g. jdoe@example.com"})
    Location = StringField('Location', validators=[DataRequired()], id="inpLocation", render_kw={"placeholder": "e.g. Kingston, Jamaica"})
    Biography = TextAreaField('Biography', validators=[DataRequired()], id="bioText")
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'PNG'], 'Images only!')],id="proPic")
    


