import mongoengine as me

class Form(me.DynamicDocument):
    name = me.StringField(required=True)
    field_list = me.ListField(required=True)
    count = me.IntField(required=True)
    companyId = me.StringField(required=True)

class Filled(me.DynamicDocument):
    company = me.StringField(required=True, max_length=30)
    formId = me.StringField(required=True)
    name = me.StringField(required=True)
    age = me.IntField(required=True)
    gender = me.StringField(required=True)