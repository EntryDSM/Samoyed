from flask import Blueprint
from flask_restful import Api


bp_excel = Blueprint("auth", __name__, url_prefix="/api/v5/admin/excel")
api_excel = Api(bp_excel)

from view.excel import Applicant
api_excel.add_resource(Applicant, "/applicant")

from view.excel import AdmissionTicket
api_excel.add_resource(AdmissionTicket, "/admission_ticket")
