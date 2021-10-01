import mongoengine as me
import jwt
import datetime
from secret import SECRET_KEY


class Company(me.Document):
    email = me.StringField(required=True, max_length=30)
    password = me.StringField()


def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms='HS256')
        pk = payload['sub']
        company = Company.objects(pk=pk).first()
        if company is None:
            return 'Company not exist'
        return company
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


class Form(me.Document):
    name = me.StringField(required=True)
    description = me.StringField()
    anonymous = me.BooleanField(required=True)
    field_list = me.ListField(required=True)
    count = me.IntField(required=True)
    company_id = me.StringField(required=True)


class Response(me.Document):
    form_id = me.StringField(required=True)
    customer_id = me.StringField()
    response_list = me.ListField(require=True)


class Customer(me.Document):
    name = me.StringField(required=True, max_length=30)
    company_id = me.StringField(required=True)
