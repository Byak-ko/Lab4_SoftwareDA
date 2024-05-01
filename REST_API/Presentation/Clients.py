from flask import Blueprint, jsonify, request
import Application.Clients as appClients

clients_api = Blueprint('clients_api', __name__)

@clients_api.get("/api/clients")
def get_clients():
    response = appClients.get_clients(request.args)
    return jsonify(response[0]), response[1]

@clients_api.get("/api/clients/<int:client_id>")
def get_client_by_id(client_id):
    response = appClients.get_client_by_id(client_id)
    return jsonify(response[0]), response[1]

@clients_api.post("/api/clients")
def make_client():
    response = appClients.make_client(request.json)
    return jsonify(response[0]), response[1]

@clients_api.delete("/api/clients/<int:client_id>")
def remove_client_by_id(client_id):
    response = appClients.remove_client_by_id(client_id)
    return jsonify(response[0]), response[1]
