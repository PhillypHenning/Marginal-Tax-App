from flask import jsonify, Blueprint

healthcheck_blueprint = Blueprint('healthcheck', __name__,)

@healthcheck_blueprint.route("/healthcheck")
def health_check():
    return jsonify({"Message": "Okay"})