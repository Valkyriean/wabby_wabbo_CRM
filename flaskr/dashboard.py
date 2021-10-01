from flask import Blueprint, request, jsonify
from flaskr.dbmodels import decode_auth_token, Form, Response


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/createform', methods=['POST'])
def create_form():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    if isinstance(company, str):
        return jsonify({"status": company})
    form = Form()
    form.company_id = str(company.pk)
    form.count = 0
    form.name = json_data["name"]
    form.description = json_data["description"]

    if json_data["anonymous"] == "True":
        form.anonymous = True
        form.field_list = json_data["field_list"]

    else:
        form.anonymous = False
        field_list = json_data["field_list"]
        form.field_list = [["Name", "String", "required"]] + field_list
    form.save()
    return jsonify({"status": "Success"})


@bp.route('/', methods=['POST'])
def homepage():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    if isinstance(company, str):
        return jsonify({"status": company})
    forms = Form.objects(company_id=str(company.pk))
    return_list = []
    for f in forms:
        temp = {}
        temp["form_id"] = str(f.pk)
        temp["count"] = f.count
        temp["name"] = f.name
        temp["description"] = f.description
        temp["anonymous"] = f.anonymous
        return_list.append(temp)
    return jsonify({"status": "Success", "forms": return_list})


@bp.route('/deleteform', methods=['POST'])
def delete_form():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    form_id = json_data['form_id']
    if isinstance(company, str):
        return jsonify({"status": company})
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    if form.company_id != str(company.pk):
        return jsonify({"status": "Unauthorized"})
    responses = Response.objects(form_id=form_id)
    for r in responses:
        r.delete()
    form.delete()
    return jsonify({"status": "Success"})


# @bp.route('/updateform', methods=['POST'])
# def update_form():
#     json_data = request.json
#     formId = json_data['form_id']
#     new_field_list = json_data['field_list']
#     token = json_data["jwt"]
#     company = decode_auth_token(token)
#     if isinstance(company, str):
#         return jsonify({"status": company})
#     form = Form.objects(pk=formId).first()
#     if form is None:
#         return jsonify({"status": "Form not exist"})
#     if form.companyany_id != str(company.pk):
#         return jsonify({"status": "Unauthorized"})
#     form.field_list = new_field_list
#     form.save()
#     return jsonify({"status": "Success"})
