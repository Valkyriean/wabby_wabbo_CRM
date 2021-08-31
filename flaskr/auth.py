from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.db_models.auth_model import Company, RegForm
from flaskr.login import login_manager

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/1', methods=('GET', 'POST'))
def test():
    Company(email="test",password="1").save()
    return "Yes"

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegForm()
    print(form.email.data)

    if request.method == 'POST':
        if form.validate():
            existing_user = Company.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                hey = Company(email=form.email.data,password=hashpass).save()
                login_user(hey)
                return redirect(url_for('auth.dashboard'))
            else:
               return f"User {form.email.data} is already registered.", 400
    return render_template('register.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    return Company.objects(pk=user_id).first()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('auth.dashboard'))
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            check_user = Company.objects(email=form.email.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('auth.dashboard'))
    return render_template('login.html', form=form)

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)

@bp.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))