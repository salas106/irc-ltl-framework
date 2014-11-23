"""
    The ``main`` module
    ===================

    Just start it and it will read the configuration file (if existing) or create one step by step (if not).
"""

import utils.config
import utils.log

logger = utils.log.get_logger('IrcBot')
conf = utils.config.get_config()

