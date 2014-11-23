"""
    The ``main`` module
    ===================

    Just start it and it will read the configuration file (if existing) or create one step by step (if not).
"""

import IrcBot.utils.log
import IrcBot.utils.config

logger = IrcBot.utils.log.get_logger('IrcBot')
conf = IrcBot.utils.config.get_config()

