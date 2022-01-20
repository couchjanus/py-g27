
import logging
from functools import wraps


def create():
    logger = logging.getLogger('exc_logger')
    logger.setLevel(logging.INFO)
    
    logfile = logging.FileHandler('exc_logger.log')
    pattern = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' 
    
    formatter = logging.Formatter(pattern)
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
    
    return logger

logger = create()

def exception(logger):
    def decor(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                issue = "Exception in " + f.__name__ + "\n"
                issue += '--------------------------------------------------------------'
                logger.exception(issue)
            raise
        return wrapper
    return decor

@exception(logger)
def div_by_zero():
    return 666/0

div_by_zero()
