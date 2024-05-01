import os
from jsonschema import validate
import Data.Services as dataServices

def get_services(args):
    services = []
    try:
        limit = args.get('limit')
        try:
            limit = int(limit)
        except Exception as e:
            limit = os.getenv("SELECT_LIMIT")
        response = dataServices.get_services(limit)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    if len(response) == 0:
        return [[{"message": "no services"}, {"status": "not found"}], 404]
    else:
        for service in response:
            services.append({
                "service_id": service[0],
                "service_name": service[1],
                "service_price": float(service[2])
            })
        return [[services, {"status": "done"}], 200]

def get_service_by_id(service_id):
    try:
        response = dataServices.get_service_by_id(service_id)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]

    if response is None:
        return [[{"data": "no service"}, {"status": "not found"}], 404]
    else:
        service = {
            "service_id": response[0],
            "service_name": response[1],
            "service_price": float(response[2])
        }
        return [[service, {"status": "done"}], 200]

def make_service(json):
    schema = {
        "type": "object",
        "properties": {
            "service_name": {"type": "string"},
            "service_price": {"type": "number"}
        },
        "required": ["service_name", "service_price"]
    }
    try:
        validate(instance=json, schema=schema)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "bad request"}], 400]

    service_name = json["service_name"]
    service_price = json["service_price"]

    try:
        dataServices.make_service(service_name, service_price)
    except Exception as e:
        return [[{"message": str(e)}, {"status": "internal error"}], 500]
    return [[{"status": "created"}], 201]

def remove_service_by_id(service_id):
    if dataServices.get_service_by_id(service_id) is None:
        return [[{"message": "no service"}, {"status": "not found"}], 404]
    else:
        try:
            dataServices.remove_service_by_id(service_id)
        except Exception as e:
            return [[{"message": str(e)}, {"status": "internal error"}], 500]
        return [[{"status": "done"}], 200]
