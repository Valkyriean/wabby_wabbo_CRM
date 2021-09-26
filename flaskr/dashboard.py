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
    forms = Form.objects(companyId=str(comp.pk))
    return jsonify(forms)


@bp.route('/deleteform', methods=['POST'])
def delete_form():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    formId = json_data['id']
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(pk=formId).first()
    if form is None:
        return jsonify({"status": "Delete Failed"})
    if form.companyId != str(comp.pk):
        return jsonify({"status": "Unauthorized"})
    form.delete()
    return jsonify({"status": "Success"})


@bp.route('/updateform', methods=['POST'])
def update_form():
    json_data = request.json
    formId = json_data['id']
    new_field_list = json_data['field_list']
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form = Form.objects(pk=formId).first()
    if form is None:
        return jsonify({"status": "Updata Failed, form is not exist"})
    if form.companyId != str(comp.pk):
        return jsonify({"status": "Unauthorized"})
    form.field_list = new_field_list
    form.save()
    return jsonify({"status": "Success"})
