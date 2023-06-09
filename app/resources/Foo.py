from flask_restful import Resource, Api
from flask import Flask, request
from app.logging.log import logger

class Foo(Resource):
    def get(self):
        logger.debug("GET Api")
        logger.info("Inside the api: "+request.base_url)
        return {"method":"get"}
    
    def post(self):
        return {"method":"post"}