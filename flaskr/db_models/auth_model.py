import mongoengine as me
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired
from flask_login import UserMixin

class Company(UserMixin, me.Document):
    # name = me.StringField(required=True, max_length=100)
    email = me.StringField(required=True, max_length=30)
    password = me.StringField()

class RegForm(FlaskForm):
    email = StringField('email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])