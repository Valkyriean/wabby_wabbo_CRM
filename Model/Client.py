from mongoengine import *

connect('crm', host='127.0.0.1', port=27017)


class Client(Document):
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    email = StringField(required=True)


john = Client(email='abc@example.com', first_name='John', last_name='Tao').save()
john.delete()
