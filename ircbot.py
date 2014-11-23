"""
    The ``main`` module
    ===================

    Just start it and it will read the configuration file (if existing) or create one step by step (if not).
"""
import sys


import irc3

import utils.log
import utils.config


logger = utils.log.get_logger('ircbot')


def create_irc_bot(config_path=None):
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
                              'irc3.plugins.human'
                          ])
    return irc_bot


bot = create_irc_bot()
bot.run()

