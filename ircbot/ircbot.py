"""
    The ``main`` module
    ===================

    Just start it and it will read the configuration file (if existing) or create one step by step (if not).
"""

import ircbot.utils.log
import ircbot.utils.config

logger = ircbot.utils.log.get_logger('ircbot')
conf = ircbot.utils.config.get_config()

