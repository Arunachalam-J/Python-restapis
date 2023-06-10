from flask import Flask
from flask_restful import Resource, Api
from app.resources.Foo import Foo
from app.resources.probes import livenessProbes, readinessProbes

app = Flask(__name__)
api = Api(app)

# Routes 
api.add_resource(Foo, '/foo')
api.add_resource(livenessProbes, '/probes/liveness')
api.add_resource(readinessProbes, '/probes/readiness')
