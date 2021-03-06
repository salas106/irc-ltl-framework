#! /usr/bin/python3
# -*- coding: utf8 -*-

"""
    The ``main`` module
    ===================

    Just start it and it will read the configuration file (if existing) or create one step by step (if not).
"""

__author__ = 'Salas'
__copyright__ = 'Copyright 2014 LTL'
__credits__ = ['Salas']
__license__ = 'MIT'
__version__ = '0.2.0'
__maintainer__ = 'Salas'
__email__ = 'Salas.106.212@gmail.com'
__status__ = 'Pre-Alpha'

import sys


import irc3

import utils.log
import utils.config


logger = utils.log.get_logger('ircbot')


def create_irc_bot(config_path=None):
    """
    Take a not mandatory path argument and create a bot with nick, server, port and default channels
    and with default core and command plugin.

    :param config_path:
    :return: irc_bot:
    :rtype:
    """

    conf = utils.config.get_config(config_path)
    try:
        bot_nick = conf['irc']['bot']['nick']
        server_host = conf['irc']['server']['host']
        server_port = conf['irc']['server']['port']
        server_ssl = conf['irc']['server']['ssl']
        public_chan = [chan['name'] for chan in conf['irc']['channels']['public']]
    except KeyError:
        sys.exit(0)

    irc_bot = irc3.IrcBot(nick=bot_nick,
                          host=server_host,
                          port=server_port,
                          ssl=server_ssl,
                          autojoins=public_chan,
                          includes=[
                              'irc3.plugins.core',
                              'irc3.plugins.command',
                              'plugins.authentication',
                              'plugins.embed'
                          ])
    return irc_bot


bot = create_irc_bot()
bot.run()

