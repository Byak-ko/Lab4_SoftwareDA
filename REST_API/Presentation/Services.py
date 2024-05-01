from flask import Blueprint, jsonify, request
import Application.Services as appServices

services_api = Blueprint('services_api', __name__)

@services_api.get("/api/services")
def get_services():
    response = appServices.get_services(request.args)
    return jsonify(response[0]), response[1]

@services_api.get("/api/services/<int:service_id>")
def get_service_by_id(service_id):
    response = appServices.get_service_by_id(service_id)
    return jsonify(response[0]), response[1]

@services_api.post("/api/services")
def make_service():
    response = appServices.make_service(request.json)
    return jsonify(response[0]), response[1]

@services_api.delete("/api/services/<int:service_id>")
def remove_service_by_id(service_id):
    response = appServices.remove_service_by_id(service_id)
    return jsonify(response[0]), response[1]
