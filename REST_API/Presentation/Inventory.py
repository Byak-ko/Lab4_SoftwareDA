from flask import Blueprint, jsonify, request
import Application.Inventory as appInventory

inventory_api = Blueprint('inventory_api', __name__)

@inventory_api.get("/api/inventory")
def get_inventory():
    response = appInventory.get_inventory(request.args)
    return jsonify(response[0]), response[1]

@inventory_api.get("/api/inventory/<int:item_id>")
def get_inventory_item_by_id(item_id):
    response = appInventory.get_inventory_item_by_id(item_id)
    return jsonify(response[0]), response[1]

@inventory_api.post("/api/inventory")
def add_inventory_item():
    response = appInventory.add_inventory_item(request.json)
    return jsonify(response[0]), response[1]

@inventory_api.delete("/api/inventory/<int:item_id>")
def remove_inventory_item_by_id(item_id):
    response = appInventory.remove_inventory_item_by_id(item_id)
    return jsonify(response[0]), response[1]
