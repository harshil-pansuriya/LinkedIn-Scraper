import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
        
    #Set level
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(handler)
    
    logger.propagate = False
    return logger