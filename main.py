from src.util.constants import *
from src.util.utilities import Get_IP_Address

from src.routes.healthcheck import healthcheck_blueprint
from src.routes.process_incometax import process_incometax_blueprint

from flask import Flask

app = Flask(__name__)

## ROUTES ##
app.register_blueprint(healthcheck_blueprint)
app.register_blueprint(process_incometax_blueprint)


if __name__ == "__main__":
    app.run(host=Get_IP_Address(), port=4000)