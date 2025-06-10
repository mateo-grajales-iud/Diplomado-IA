from flask import Blueprint, jsonify, request, current_app, g
from app.services.QueryServices import ParseRequestData

api_routes = Blueprint('api', __name__, url_prefix='/api')

@api_routes.route('/status')
def status():
    return jsonify({"status": "ok"})

@api_routes.route('/query', methods=['POST'])
def postQuery():
    current_app.logger.info("POST received on /query")
    current_app.logger.info(f"Payload: {request.form.to_dict()}")
    dataRaw = request.form.to_dict()
    data = ParseRequestData(dataRaw)
    current_app.logger.info(f"Parsed and stored query: {data}")
    
    return jsonify({
        "id" : data["id"],
        "status" : data["status"]
    }), 200
