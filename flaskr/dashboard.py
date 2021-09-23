from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.db_models.auth_model import Company
from flaskr.db_models.dashboard_model import Form, Filled
from flaskr.setup import login_manager


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/createform', methods=['POST'])
@login_required
def create_form():
    json_data = request.json
    # json_data["count"] = 0
    # json_data["companyId"] = current_user.pk
    form = Form()
    form.companyId = str(current_user.pk)
    print(type(current_user.pk))
    form.count = 0
    form.name = json_data["name"]
    form.field_list = json_data["field_list"]
    form.save()
    return jsonify({"status": "Success"})

    

'''





'''
