from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.dbmodels import *
from email_validator import validate_email, EmailNotValidError

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    json_data = request.json
    email = json_data['email'].lower()
    password = json_data['password']
    error = None
    if not email:
        error = 'Email is required.'
    elif not password:
        error = 'Password is required.'
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError as e:
        error = str(e)
    if error is None:
        existing_user = Company.objects(email=email).first()
        if existing_user is None:
            company = Company()
            company.email = email
            company.password = generate_password_hash(password)
            company.save()
            token = encode_auth_token(str(company.pk))
            return jsonify({"status": "Success", "jwt": token})
        else:
            error = 'Email already registered.'
    return jsonify({"status": error})


@bp.route('/login', methods=['POST'])
def login():
    json_data = request.json
    email = json_data['email'].lower()
    password = json_data['password']
    error = None
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError as e:
        error = str(e)
    company = Company.objects(email=email).first()
    if company is None:
        error = 'Incorrect email.'
    elif not check_password_hash(company['password'], password):
        error = 'Incorrect password.'
    if error is None:
        token = encode_auth_token(str(company.pk))
        return jsonify({"status": "Success", "jwt": token})
    return jsonify({"status": error})


@bp.route('/changepass', methods=['POST'])
def change_password():
    json_data = request.json
    token = json_data["jwt"]
    password = json_data['password']
    new_password = json_data['new_password']
    company = decode_auth_token(token)
    error = None
    if isinstance(company, str):
        error = company
    elif company is None:
        error = 'User not exist.'
    elif not check_password_hash(company['password'], password):
        error = 'Incorrect password.'
    if error is None:
        company.password = (generate_password_hash(new_password))
        company.save()
        return jsonify({"status": "Success"})
    return jsonify({"status": error})


@bp.route('/deleteaccount', methods=['POST'])
def delete_account():
    json_data = request.json
    token = json_data["jwt"]
    password = json_data['password']
    company = decode_auth_token(token)
    error = None
    if isinstance(company, str):
        error = company
    elif company is None:
        error = 'User not exist.'
    elif not check_password_hash(company['password'], password):
        error = 'Incorrect password.'
    if error is None:
        company.delete()
        return jsonify({"status": "Success"})
    return jsonify({"status": error})
