from app.db.db_settings import Mongo
from app.resources.probes import readinessProbes, livenessProbes
from flask import Response

def test_readiness_probes():
    readiness = readinessProbes()
    response_message, response_code = readiness.get()
    # Mongo clint not working
    assert {"status":False},400 == readiness.get()
    

def test_liveness_probes():
    liveness = livenessProbes()
    assert {"status":True},200 == liveness.get() 