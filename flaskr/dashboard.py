from flask import Blueprint, request, jsonify
from flaskr.dbmodels import decode_auth_token, Form, Response


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/createform', methods=['POST'])
def create_form():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form()
    form.companyId = str(comp.pk)
    form.count = 0
    form.name = json_data["name"]
    form.description = json_data["description"]
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
    forms = Form.objects(companyId=str(comp.pk))
    return_list = []
    for f in forms:
        temp = {}
        temp["form_id"] = str(f.pk)
        temp["count"] = f.count
        temp["name"] = f.name
        temp["description"] = f.description
        return_list.append(temp)
    return jsonify({"status": "Success", "forms": return_list})


@bp.route('/deleteform', methods=['POST'])
def delete_form():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    formId = json_data['form_id']
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(pk=formId).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    if form.companyId != str(comp.pk):
        return jsonify({"status": "Unauthorized"})
    form.delete()
    return jsonify({"status": "Success"})


@bp.route('/updateform', methods=['POST'])
def update_form():
    json_data = request.json
    formId = json_data['form_id']
    new_field_list = json_data['field_list']
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(pk=formId).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    if form.companyId != str(comp.pk):
        return jsonify({"status": "Unauthorized"})
    form.field_list = new_field_list
    form.save()
    return jsonify({"status": "Success"})
