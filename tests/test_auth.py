import pytest
from flask import g, session
from flask import session
from flask import request, url_for
from flaskr.dbmodels import Company
from mongoengine import *

@pytest.mark.parametrize(('email', 'password'), (
    ('ccc@gmail.com', 'aaaa3333'),
))
def test_register(client, db, app, email, password):
    
    with app.app_context():
        existing_user = Company.objects(email=email).first()
        assert existing_user is None
    # test that viewing the page renders without template errors
    assert client.get("/app/register").status_code == 200

    # test that successful registration redirects to the dashboard
    response = client.post("/app/register", data={"email": email, "password": password}, follow_redirects=True)
    assert response.status == '200 OK'

    assert response.request.path == "/app/dashboard"
    # assert "http://localhost/auth/dashboard" == response.headers["location"]

    # test that the user was inserted into the database
    with app.app_context():
        existing_user = Company.objects(email=email).first()
        assert existing_user is not None

@pytest.mark.parametrize(('email', 'password', 'message'), (
    ('', '', b'Email is required.'),
    ('a', '', b'Password is required.'),
    ('test@163.com', 'cccc3333', b'Email already registered.'),
))
def test_register_validate_input(client, email, password, message):
    response = client.post(
        '/app/register',
        data={'email': email, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get("/app/login").status_code == 200

    # test that successful login redirects to the index page
    # objs = Company.objects
    # print(objs.to_json())

    response = auth.login()
    assert response.request.path == "/app/dashboard"
    #assert response.headers["Location"] == "http://localhost/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    client.get("/")
    assert '_user_id' in session
    # with client:
    #     client.get("/")
    #     assert session["user_id"] == 1
    #     assert g.user["email"] == "test@163.com"

@pytest.mark.parametrize(
    ("email", "password", "message"),
    (("a", "test", b"Incorrect email."), ("test@163.com", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, email, password, message):
    response = auth.login(email, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()
    auth.logout()
    assert 'user_id' not in session
    # with client:
    #     auth.logout()
    #     assert 'user_id' not in session