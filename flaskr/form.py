from dns.rdataclass import NONE
from flask import Blueprint, request, jsonify
from flaskr.dbmodels import decode_auth_token, Form, Response, Customer

bp = Blueprint('form', __name__, url_prefix='/form')


@bp.route('/getform', methods=['POST'])
def get_form():
    json_data = request.json
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    field_list = form.field_list
    name = form.name
    description = form.description
    return jsonify({"status": "Success", "field_list": field_list, "name": name, "description": description})


@bp.route('/saveresponse', methods=['POST'])
def save_response():
    json_data = request.json
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    form.count += 1
    form.save()
    response = Response()
    response.form_id = form_id
    response_list = json_data['response_list']
    if not form.anonymous:
        name = response_list[0]
        customer = Customer.objects(
            name=name, company_id=form.company_id).first()
        if customer is None:
            customer = Customer()
            customer.name = name
            customer.company_id = form.company_id
            customer.save()
        response.customer_id = str(customer.pk)
        response.response_list = response_list
    else:
        response.response_list = response_list
    response.save()
    return jsonify({"status": "Success"})


@bp.route('/deleteresponse', methods=['POST'])
def delete_response():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    responseId = json_data['response_id']
    if isinstance(company, str):
        return jsonify({"status": company})
    response = Response.objects(pk=responseId).first()
    if response is None:
        return jsonify({"status": "Response Not Exist"})
    form_id = response.form_id
    form = Form.objects(pk=form_id).first()
    form.count += -1
    response.delete()
    form.save()
    return jsonify({"status": "Success"})


@bp.route('/showresponse', methods=['POST'])
def show_response():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    if isinstance(company, str):
        return jsonify({"status": company})
    form_id = json_data['form_id']
    form = Form.objects(pk=form_id).first()
    if form is None:
        return jsonify({"status": "Form not exist"})
    header = []
    for l in form.field_list:
        header.append(str(l["question_name"]))
    responses = Response.objects(form_id=str(form_id))
    return_list = []
    for r in responses:
        temp = {}
        temp["response_id"] = str(r.pk)
        temp["response"] = r.response_list
        if not form.anonymous:
            temp["customer_id"] = r.customer_id
        return_list.append(temp)
    return jsonify({"status": "Success", "name": form.name, "description": form.description, "anonymous": form.anonymous, "field_list": header, "responses": return_list})


@bp.route('/checkcustomer', methods=['POST'])
def check_customer():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    if isinstance(company, str):
        return jsonify({"status": company})
    customer_id = json_data['customer_id']
    customer = Customer.objects(pk=customer_id).first()
    if customer is None:
        return jsonify({"status": "Customer not exist"})
    if customer.company_id != str(company.pk):
        return jsonify({"status": "Customer not accessible"})
    responses = Response.objects(customer_id=customer_id)
    return_list = []
    for r in responses:
        temp = {}
        form = Form.objects(pk=r.form_id).first()
        if form is None:
            return jsonify({"status": "Form not exist"})
        header = []
        for l in form.field_list:
            header.append(str(l["question_name"]))
        temp["field_list"] = header
        temp["response_id"] = str(r.pk)
        temp["response"] = r.response_list
        return_list.append(temp)
    return jsonify({"status": "Success", "responses": return_list})


@bp.route('/getcustomer', methods=['POST'])
def get_customer():
    json_data = request.json
    token = json_data["jwt"]
    company = decode_auth_token(token)
    if isinstance(company, str):
        return jsonify({"status": company})
    customer = Customer.objects(company_id=str(company.pk))
    if customer is None:
        return jsonify({"status": "Customer not exist"})
    return_list = []
    for c in customer:
        temp = {}
        temp["name"] = c.name
        temp["customer_id"] = str(c.pk)
        return_list.append(temp)
    return jsonify({"status": "Success", "responses": return_list})
