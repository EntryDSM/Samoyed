import datetime
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request

from samoyed.controller.applicant import create_applicant_excel
from samoyed.controller.admission_ticket import create_admission_ticket
from samoyed.controller.competition_status import create_competition_status_excel


class AdmissionTicket(Resource):

    @jwt_required
    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        return create_admission_ticket(date)


class Applicant(Resource):

    @jwt_required
    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        return create_applicant_excel(date)


class CompetitionStatus(Resource):

    @jwt_required
    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        token = request.headers['Authorization']

        return create_competition_status_excel(date, token)
