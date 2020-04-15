"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os, datetime, random
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from app.models import UserProfile
from werkzeug.security import check_password_hash
from app.form import ProfileForm
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')





@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')





@app.route('/profile', methods=['POST','GET'])
def profile():
    """ Render the website's profile form """
    form = ProfileForm()
    if (request.method == "POST" and form.validate_on_submit()):
        fname = form.Fname.data
        lname = form.Lname.data
        gender = form.Gender.data
        email = form.Email.data
        location = form.Location.data
        biography = form.Biography.data
        photo = request.files['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        jTime = datetime.date.today()
        joined = jTime.strftime("%B %d, %Y") 
        userID = userIDGenerate(fname,lname)
        user = UserProfile(fname,lname,gender,email,location,biography,filename,userID,joined)
        db.session.add(user)
        db.session.commit()
        flash('User has been created and added!', 'success')
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)





@app.route('/profiles', methods=["GET", "POST"])
def profiles():
    """ Renders list of profiles on website """
    users = UserProfile.query.all()
    if request.method == "GET":
        return render_template("profiles.html", users=users)





@app.route('/profile/<userID>', methods=["GET", "POST"])
def getProfile(userID):
    """ Renders profile given the userID """
    user = UserProfile.query.filter_by(userID=userID).first()
    return render_template("myProfile.html", user=user)





def userIDGenerate(fname,lname):
    """ This functions is for viewing an individual user profile by the specific user's id """
    return fname + lname + str(random.randint(5,99))



@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    

    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
