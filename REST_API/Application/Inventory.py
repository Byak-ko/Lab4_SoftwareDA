import os
from jsonschema import validate
import Data.Inventory as dataInventory

def get_inventory(args):
    inventory_items = []
    try:
        limit = args.get('limit')
        try:
            limit = int(limit)
        except Exception as e:
            limit = os.getenv("SELECT_LIMIT")
        response = dataInventory.get_inventory(limit)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    if len(response) == 0:
        return [[{"message": "no inventory items"}, {"status": "not found"}], 404]
    else:
        for item in response:
            inventory_items.append({
                "item_id": item[0],
                "item_name": item[1],
                "item_quantity": int(item[2]),
                "item_price": float(item[3])
            })
        return [[inventory_items, {"status": "done"}], 200]

def get_inventory_item_by_id(item_id):
    try:
        response = dataInventory.get_inventory_item_by_id(item_id)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]

    if response is None:
        return [[{"data": "no inventory item"}, {"status": "not found"}], 404]
    else:
        inventory_item = {
            "item_id": response[0],
            "item_name": response[1],
            "item_quantity": int(response[2]),
            "item_price": float(response[3])
        }
        return [[inventory_item, {"status": "done"}], 200]

def add_inventory_item(json):
    schema = {
        "type": "object",
        "properties": {
            "item_name": {"type": "string"},
            "item_quantity": {"type": "integer", "minimum": 0},
            "item_price": {"type": "number", "minimum": 0}
        },
        "required": ["item_name", "item_quantity", "item_price"]
    }
    try:
        validate(instance=json, schema=schema)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "bad request"}], 400]

    item_name = json["item_name"]
    item_quantity = json["item_quantity"]
    item_price = json["item_price"]

    try:
        dataInventory.add_inventory_item(item_name, item_quantity, item_price)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    return [[{"status": "created"}], 201]

def remove_inventory_item_by_id(item_id):
    if dataInventory.get_inventory_item_by_id(item_id) is None:
        return [[{"message": "no inventory item"}, {"status": "not found"}], 404]
    else:
        try:
            dataInventory.remove_inventory_item_by_id(item_id)
        except Exception as e:
            return [[{"message": str(e)}, {"status": "internal error"}], 500]
        return [[{"status": "done"}], 200]
