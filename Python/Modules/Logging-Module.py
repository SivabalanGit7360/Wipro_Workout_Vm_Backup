# what is log - recording of events
# why we need to create a log

# import logging - (module used for generating logs)
# debug - low
# info
# warning
# critical - high

import logging

logging.basicConfig(level=logging.DEBUG, filename="message.log", filemode='w')
logger = logging.getLogger('sampler-logger')

logger.debug("this is a debug log")
logger.info("this is a informational log")
logger.warning("this is a warning log")
logger.critical("this is critical log")