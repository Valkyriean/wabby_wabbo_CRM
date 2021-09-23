from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.dbmodels import Company, decode_auth_token
from flaskr.dbmodels import Form, Filled


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/createform', methods=['POST'])
def create_form():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    # json_data["count"] = 0
    # json_data["companyId"] = current_user.pk
    form = Form()
    form.companyId = str(comp.pk)
    print(type(comp.pk))
    form.count = 0
    form.name = json_data["name"]
    form.field_list = json_data["field_list"]
    form.save()
    return jsonify({"status": "Success"})

    
@bp.route('/', methods=['POST'])
def homepage():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    forms = Form.objects(companyId = comp.pk)
    return jsonify(forms)


@bp.route('/deleteform', methods=['POST'])
def delete_form():
    json_data = request.json
    formId = json_data['id']
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(compaynId = comp.pk, formId = formId)
    if form is None:
        return jsonify({"status": "Delete Failed"})
    form.delete()
    return jsonify({"status": "Success"})

@bp.route('/updataform', methods=['POST'])
def updata_form():
    json_data = request.json
    formId = json_data['id']
    new_field_list = json_data['field_list']
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(compaynId = comp.pk, formId = formId)
    if form is None:
        return jsonify({"status": "Updata Failed, form is not exist"})
    form.field_list = new_field_list 
    form.save()
    return jsonify({"status": "Success"})





