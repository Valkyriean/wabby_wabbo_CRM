from mongoengine import *



class BasicForm(Document):
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    email = StringField(required=True)


form = BasicForm(first_name = 'aaa', last_name = 'bbb', email = '123@.com').save()
form.delete()
