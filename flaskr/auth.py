from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.db_models.auth_model import Company
from flaskr.setup import login_manager


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
            hey = comp.save()
            login_user(hey)
            return jsonify({"status": "Success"})
        else:
            error = 'Email already registered.'
    return jsonify({"status": error})


@login_manager.user_loader
def load_user(user_id):
    return Company.objects(pk=user_id).first()


@bp.route('/login', methods=['POST'])
def login():
    print(current_user.pk)
    if current_user.is_authenticated == True:
        return jsonify({"status": "Already logged in"})
    json_data = request.json
    email = json_data['email']
    password = json_data['password']
    rememberMe = (json_data['rememberMe'] == "True")
    error = None
    user = Company.objects(email=email).first()
    if user is None:
        error = 'Incorrect email.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'
    if error is None:
        login_user(user, remember=rememberMe)
        return jsonify({"status": "Success"})
    return jsonify({"status": error})


# @bp.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', name=current_user.email)


@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"status": "Success"})
