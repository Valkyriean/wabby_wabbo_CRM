from dns.rdataclass import NONE
from flask import Blueprint, request, jsonify
from flaskr.dbmodels import decode_auth_token, Form, Response

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('/getform', methods=['POST'])
def getform():
    json_data = request.json
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    fieldlist = form.field_list
    return jsonify({"status": "Success", "field_list": fieldlist})


@bp.route('/saveresponse', methods=['POST'])
def saveresponse():
    json_data = request.json
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    form.count += 1
    form.save()
    response = Response()
    response.formId = form_id
    response.response_list = json_data['response_list']
    response.save()
    return jsonify({"status": "Success"})


@bp.route('/deleteresponse', methods=['POST'])
def deleteresponse():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    responseId = json_data['response_id']
    if isinstance(comp, str):
        return jsonify({"status": comp})
    response = Response.objects(pk=responseId).first()
    if response is None:
        return jsonify({"status": "Response Not Exist"})
    form_id = response.formId
    form = Form.objects(pk=form_id).first()
    form.count += -1
    response.delete()
    form.save()
    return jsonify({"status": "Success"})


@bp.route('/showresponse', methods=['POST'])
def showresponse():
    json_data = request.json
    token = json_data["jwt"]
    comp = decode_auth_token(token)
    if isinstance(comp, str):
        return jsonify({"status": comp})
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    responses = Response.objects(formId=str(form_id))
    return_list = []
    for r in responses:
        temp = {}
        temp["response_id"] = str(r.pk)
        temp["response"] = r.response_list
        return_list.append(temp)
    return jsonify({"status": "Success", "name": form.name, "description": form.description, "field_list": form.field_list, "responses": return_list})
