from flaskr.model import *
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('auth', __name__, url_prefix='/auth')

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
                # login_user(hey)
                return "Register complete"
            else:
                error = f"User {form.email.data} is already registered."
                flash(error)
    return render_template('register.html', form=form)