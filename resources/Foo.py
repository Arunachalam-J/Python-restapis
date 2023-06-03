from flask_restful import Resource, Api
from flask import Flask

class Foo(Resource):
    def get(self):
        return {"method":"get"}
    
    def post(self):
        return {"method":"post"}