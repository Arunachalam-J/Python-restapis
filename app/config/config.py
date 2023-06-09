from functools import cache
import json
from app.logging.log import logger

@cache
def get_config(path:str)-> dict():
    try:
        with open(path) as f:
            return json.dumps(f.read())
    except Exception as exp:
        logger.error(exp)
        return None
    
