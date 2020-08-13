import datetime
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_raw_jwt
from flask import request

from controller.applicant import create_applicant_excel
from controller.admission_ticket import create_admission_ticket
from controller.competition_status import create_competition_status_excel


class AdmissionTicket(Resource):
    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        return create_admission_ticket(date)


class Applicant(Resource):
    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        return create_applicant_excel(date)


class CompetitionStatus(Resource):
    @jwt_required
    def post(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        token = get_raw_jwt()

        return create_competition_status_excel(date, token)
