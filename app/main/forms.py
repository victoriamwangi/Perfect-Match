from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class PostPic(FlaskForm):
    feed_picture = FileField('feed picture', validators=[FileAllowed(['jpg','png'])])
    caption = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Update')

    

