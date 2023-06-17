from flask import Response,jsonify
from flask_restful import Resource, Api
from app.db.db_settings import Mongo
from app.logging.log import logger

class readinessProbes(Resource):
    def get(self):
        try:
            Mongo("192.168.0.107",27017).get_client().server_info()
            logger.debug("Readiness Probes ----  ")
            return {
                "status":True
                },200
        except Exception as exp:
            logger.error(exp)
            return {
                "status":False
                },400

class livenessProbes(Resource):
    def get(self):
        try:
            return {
                "status":True
                },200
        except Exception as exp:
            logger.error(exp)
            return {
                "status":False
                },400