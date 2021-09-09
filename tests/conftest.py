import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.setup import login_manager, db
import mongoengine
from flask_mongoengine import MongoEngine
from mongoengine import connect
from mongoengine.connection import disconnect
from flaskr.db_models.auth_model import Company
from werkzeug.security import check_password_hash, generate_password_hash

@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    with app.app_context():
        yield app
    mongoengine.connection.disconnect_all()


@pytest.fixture()
def db(app):
    # disconnect master mongodb 
    disconnect()
    # reset testing mongodb
    app.config['MONGODB_SETTINGS'] = {
        "db": "crm_test_db",
        'host': 'localhost',
        'port': 27017
    }
    test_db = MongoEngine(app)
    # insert a test data into db
    comp = Company()
    comp.email = "test@163.com"
    comp.password = generate_password_hash("cccc3333")
    comp.save()
    
    yield test_db

    # Clear database after tests, for graceful exit.
    Company.drop_collection()
    test_db.connection.drop_database("crm_test_db")


@pytest.fixture
def client(app):
    # Prepare before your test
    with app.test_client() as client:
        # Give control to your test
        yield client


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, email='test@163.com', password='cccc3333'):
        return self._client.post('/auth/login', data={'email': email, 'password': password}, follow_redirects=True)

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)