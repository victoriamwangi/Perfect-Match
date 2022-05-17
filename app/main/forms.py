from flask_wtf  import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField,SelectField,IntegerField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    username =StringField("Username",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    gender =SelectField('Gender', choices=[('Male','Male'), ('Female', 'Female')],
                           validators=[DataRequired()])

    occupation = TextAreaField("Occupation",validators=[DataRequired()])
    age = IntegerField("Age",validators=[DataRequired()])
    location = TextAreaField("Location",validators=[DataRequired()])
    race= TextAreaField("Race",validators=[DataRequired()])
    bio = TextAreaField("Bio",validators=[DataRequired()])
    
    submit = SubmitField("Update",validators=[DataRequired()]) 

