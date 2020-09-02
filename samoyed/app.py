from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from samoyed.config import JWT_SECRET_KEY
from samoyed.router import bp_excel


def create_app():

    _app = Flask(__name__)

    CORS(_app, resources={
        r"/api/*": {"origin": "*"}
    })

    _app.register_blueprint(bp_excel)

    _app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

    JWTManager(app=_app)

    return _app
