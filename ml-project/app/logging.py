import logging
import sys

# Gets or creates a logger
logger = logging.getLogger('app')  

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
sdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.handlers.TimedRotatingFileHandler('/app/log/log.log', when="midnight", interval=1)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
sdout_handler.setFormatter(formatter)
# add file handler to logger
logger.addHandler(file_handler)
logger.addHandler(sdout_handler)