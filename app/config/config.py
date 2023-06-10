from functools import cache
import json
from app.logging.log import logger

@cache
def get_config()-> dict():
    try:
        with open("app/config/configuration.json","r") as f:
            return json.loads(f.read())
    except Exception as exp:
        logger.error(exp)
        return None
    
