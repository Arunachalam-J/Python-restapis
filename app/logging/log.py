import logging
from logging.handlers import RotatingFileHandler
import time

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# handler = RotatingFileHandler("Flask.log", maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

log_handler = logging.handlers.WatchedFileHandler('Flask.log')
formatter = logging.Formatter(
        '%(asctime)s  [%(levelname)s]: %(message)s',
        '%b %d %H:%M:%S')
formatter.converter = time.gmtime  # if you want UTC time
log_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)