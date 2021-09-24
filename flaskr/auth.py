from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.dbmodels import *


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    json_data = request.json
    email = json_data['email']
    password = json_data['password']
    error = None
    if not email:
        error = 'Email is required.'
    elif not password:
        error = 'Password is required.'
    if error is None:
        existing_user = Company.objects(email=email).first()
        if existing_user is None:
            comp = Company()
            comp.email = email
            comp.password = generate_password_hash(password)
            comp.save()
            token = encode_auth_token(str(comp.pk))
            return jsonify({"status": "Success", "jwt": token})

        else:
            error = 'Email already registered.'
    return jsonify({"status": error})


# @login_manager.user_loader
# def load_user(user_id):
#     return Company.objects(pk=user_id).first()


@bp.route('/login', methods=['POST'])
def login():
    json_data = request.json
    email = json_data['email']
    password = json_data['password']
    error = None
    comp = Company.objects(email=email).first()
    if comp is None:
        error = 'Incorrect email.'
    elif not check_password_hash(comp['password'], password):
        error = 'Incorrect password.'
    if error is None:
        token = encode_auth_token(str(comp.pk))
        return jsonify({"status": "Success", "jwt": token})
    return jsonify({"status": error})


# @bp.route('/unauthorized', methods=['GET'])
# def unauthorized():
#     return jsonify({"status": "unauthorized"})


# @bp.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', name=current_user.email)


# @bp.route('/logout', methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"status": "Success"})


@bp.route('/changepass', methods=['POST'])
def change_password():
    json_data = request.json
    token = json_data["jwt"]
    password = json_data['password']
    new_password = json_data['new_password']
    comp = decode_auth_token(token)
    error = None
    if isinstance(comp, str):
        error = comp
    elif comp is None:
        error = 'User not exist.'
    elif not check_password_hash(comp['password'], password):
        error = 'Incorrect password.'
    if error is None:
        comp.password = (generate_password_hash(new_password))
        comp.save()
        return jsonify({"status": "Success"})
    return jsonify({"status": error})


@bp.route('/deleteaccount', methods=['POST'])
def delete_account():
    json_data = request.json
    token = json_data["jwt"]
    password = json_data['password']
    comp = decode_auth_token(token)
    error = None
    if isinstance(comp, str):
        error = comp
    elif comp is None:
        error = 'User not exist.'
    elif not check_password_hash(comp['password'], password):
        error = 'Incorrect password.'
    if error is None:
        comp.delete()
        return jsonify({"status": "Success"})
    return jsonify({"status": error})
