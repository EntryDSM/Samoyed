import datetime
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from controller.applicant import create_applicant_excel


class AdmissionTicket(Resource):
    pass


class Applicant(Resource):

    def get(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

        return create_applicant_excel(date)


class CompetitionStatus(Resource):
    pass