from mongoengine import *

class Client(Document):
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    email = StringField(required=True)

def create():
    john = Client(email='abc@example.com', first_name='John', last_name='Tao').save()