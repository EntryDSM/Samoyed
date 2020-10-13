import json_logging

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from logging.handlers import RotatingFileHandler

from samoyed.config import JWT_SECRET_KEY
from samoyed.router import bp_excel


def create_app():

    _app = Flask(__name__)

    CORS(_app, resources={
        r"/api/*": {"origin": "*"}
    })

    _app.register_blueprint(bp_excel)

    _app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(_app)

    request_logger = json_logging.get_request_logger()
    handler = RotatingFileHandler(filename='samoyed/log/log.json', maxBytes=5000000, backupCount=10)
    handler.setFormatter(json_logging.JSONRequestLogFormatter())
    request_logger.addHandler(handler)

    JWTManager(app=_app)

    return _app
