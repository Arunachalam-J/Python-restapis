from flask import Flask
from flask_restful import Resource, Api
from pyrestapis.resources.Foo import Foo

app = Flask(__name__)
api = Api(app)

# Routes 
api.add_resource(Foo, '/foo')