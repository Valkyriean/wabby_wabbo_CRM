from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.db_models.auth_model import Company
from flaskr.setup import login_manager

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/1', methods=('GET', 'POST'))
def test():
    Company(email="test",password="1").save()
    return "Yes"

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form['remember-me']
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
                login_user(hey, remember=remember)
                return redirect(url_for('auth.dashboard'))
            else:
                error = 'Email already registered.'
        flash(error)
    return render_template('register.html')

@login_manager.user_loader
def load_user(user_id):
    return Company.objects(pk=user_id).first()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('auth.dashboard'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None 
        user = Company.objects(email=email).first()
        if user is None:
            error = 'Incorrect email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        if error is None:
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash(error)
    return render_template('login.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)

@bp.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))