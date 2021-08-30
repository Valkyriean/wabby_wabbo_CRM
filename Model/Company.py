from mongoengine import *



class Company(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True)


unimelb = Company(name='Unimelb', email='unimelb@unimelb.edu.au').save()
unimelb.delete()
