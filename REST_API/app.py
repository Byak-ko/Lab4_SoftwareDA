from dotenv import load_dotenv

from flask import Flask
from Presentation.Clients import clients_api
from Presentation.Services import services_api
from Presentation.Inventory import inventory_api

load_dotenv()

# application   
app = Flask(__name__)

app.json.sort_keys = False

app.register_blueprint(clients_api)

app.register_blueprint(services_api)

app.register_blueprint(inventory_api)


app.run()