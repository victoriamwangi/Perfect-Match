from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(85), nullable= False)
    email = db.Column(db.String(255), unique=True, index= True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    race = db.Column(db.String(10))
    occupation = db.Column(db.String(85))
    location = db.Column(db.String(255))
    posts = db.relationship('Images',backref='users',passive_deletes=True)
    comments = db.relationship('Comment',backref='users',passive_deletes=True)
    likes = db.relationship('Like',backref='users',passive_deletes=True)

    
    @property
    def password(self): 
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


class Comment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime(timezone=False),default=func.now())
    author = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('images.id'),nullable=False)


class Like(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('images.id'),nullable=False)


    
class Images(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    caption= db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    author=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref='images',passive_deletes=True)
    likes = db.relationship('Like',backref='images',passive_deletes=True)
    
