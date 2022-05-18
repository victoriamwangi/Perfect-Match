import os	
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_login import login_required
from ..models import User,Post,Like,Comment
from .forms import UpdateProfile
from .. import db, photos
from . import main
from .app import app


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/')
def index():
    return render_template('index.html')

	

@main.route('/postpic', methods=['POST','GET'])
def postpic():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	return render_template('postpic.html', filenames=file_names)

# @main.route('/display/<filename>')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='uploads/' + filename))




#user profile
@main.route('/user/<username>')
def profile(username):
   user = User.query.filter_by(username=username).first()

   return render_template("profile/profile.html", user = user)

#update profile
@main.route('/user/<username>/update',methods =['GET','POST'])
@login_required
def update_profile(username):
   user = User.query.filter_by(username = username).first()

   form = UpdateProfile()
   if form.validate_on_submit():
        
        username= form.username.data
        user.email = form.email.data
        user.race = form.race.data
        user.age = form.age.data
        user.gender = form.gender.data
        user.location = form.location.data
        user.occupation = form.occupation.data
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',username=user.username))

   return render_template('profile/update.html',form =form)

#profile pic
# @main.route('/user/<username>/update/pic',methods=['POST'])
# @login_required
# def update_pic(username):
#    user = User.query.filter_by(username=username).first()
#    if 'photo' in request.files:
#       filename = photos.save(request.files['photo'])
#       path = f'photos/{filename}'
#       user.profile_pic_path = path
#       db.session.commit()
#    return redirect(url_for('main.profile',username=username))
