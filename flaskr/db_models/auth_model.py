import mongoengine as me
from flask_login import UserMixin

class Company(UserMixin, me.Document):
    # name = me.StringField(required=True, max_length=100)
    email = me.StringField(required=True, max_length=30)
    password = me.StringField()
