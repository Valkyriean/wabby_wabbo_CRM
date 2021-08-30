from mongoengine import *

connect('crm', host='127.0.0.1', port=27017)


class Company(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True)


unimelb = Company(name='Unimelb', email='unimelb@unimelb.edu.au').save()
unimelb.delete()
