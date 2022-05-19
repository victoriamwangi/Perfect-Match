from flask import render_template,redirect,url_for,request,redirect
from flask_login import login_required, current_user
from ..models import User,Post,Like,Comment, Images
from .forms import UpdateProfile, UploadForm
from .. import db, photos
from . import main
from werkzeug.utils import secure_filename
from app import create_app
import os

app = create_app('development')


@main.route('/')
def index():
    return render_template('index.html')

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
@main.route('/user/<username>/update/pic',methods=['POST'])
@login_required
def update_pic(username):
   user = User.query.filter_by(username=username).first()
   if 'photo' in request.files:
      filename = photos.save(request.files['photo'])
      path = f'photos/{filename}'
      user.profile_pic_path = path
      db.session.commit()
   return redirect(url_for('main.profile',username=username))

@main.route("/uploadimage",methods=["POST","GET"])
@login_required
def uploadimage():
    user=current_user
    frm=UploadForm()
    if frm.validate_on_submit():
        file=request.files["file"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
        upload=Images(name=secure_filename(file.filename),uploader_id=user.id)
        db.session.add(upload)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("imageupload.html",upload_form=frm,user=user.username)
 
# @main.route("/viewallimages",methods=["POST","GET"])
# @login_required
# def viewallimages():
#     allimages=Images.query.all()
#     return render_template("viewall.html",images=allimages)