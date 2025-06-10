from flask import Blueprint, render_template, g
from app.routes.routes_data.FormFields import FormFields
from app.services.QueryServices import GetRequestData
from app.utils.JSONParser import cleanJson
from app.utils.Constants import *

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    fields = FormFields()
    return render_template('main.html', fields=fields)

@main_routes.route('/result/<int:queryId>')
def getResults(queryId):
    data = GetRequestData(queryId)
    json = None
    if (data['status'] == COMPLETED):
        json = cleanJson(data["response"])
    return render_template('results.html', status=data["status"], data=data, json=json, title="Plan de Alimentación")

@main_routes.app_template_filter("formatear")
def formatear_clave(clave):
    return ' '.join(clave.split('_')).capitalize()