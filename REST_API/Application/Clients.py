import os
from jsonschema import validate
import Data.Clients as dataClients

def get_clients(args):
    clients = []
    try:
        limit = args.get('limit')
        try:
            limit = int(limit)
        except Exception as e:
            limit = os.getenv("SELECT_LIMIT")
        response = dataClients.get_clients(limit)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    if len(response) == 0:
        return [[{"message": "no clients"}, {"status": "not found"}], 404]
    else:
        for client in response:
            clients.append({
                "client_id": client[0],
                "client_name": client[1],
                "client_phone": client[2]
            })
        return [[clients, {"status": "done"}], 200]

def get_client_by_id(client_id):
    try:
        response = dataClients.get_client_by_id(client_id)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]

    if response is None:
        return [[{"data": "no client"}, {"status": "not found"}], 404]
    else:
        client = {
            "client_id": response[0],
            "client_name": response[1],
            "client_phone": response[2]
        }
        return [[client, {"status": "done"}], 200]

def make_client(json):
    schema = {
        "type": "object",
        "properties": {
            "client_name": {"type": "string"},
            "client_phone": {"type": "string"}
        },
        "required": ["client_name", "client_phone"]
    }
    try:
        validate(instance=json, schema=schema)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "bad request"}], 400]

    client_name = json["client_name"]
    client_phone = json["client_phone"]

    try:
        dataClients.make_client(client_name, client_phone)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    return [[{"status": "created"}], 201]

def remove_client_by_id(client_id):
    if dataClients.get_client_by_id(client_id) is None:
        return [[{"message": "no client"}, {"status": "not found"}], 404]
    else:
        try:
            dataClients.remove_client_by_id(client_id)
        except Exception as e:
            return [[{"message": str(e)}, {"status": "internal error"}], 500]
        return [[{"status": "done"}], 200]
