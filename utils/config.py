# -*- coding: utf8 -*-

"""
    The ``config`` module
    ===================

    Create a named logger and  return it so users can log in different log files : one for each module.
"""

__author__ = 'Salas'
__copyright__ = 'Copyright 2014 LTL'
__credits__ = ['Salas']
__license__ = 'MIT'
__version__ = '0.2.0'
__maintainer__ = 'Salas'
__email__ = 'Salas.106.212@gmail.com'
__status__ = 'Pre-Alpha'

import os
import os.path as path
import errno
import sys

import yaml

from yaml import CLoader as Loader, CDumper as Dumper


import utils.log

logger = utils.log.get_logger('config')

CONFIG_DIR_PATH = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, 'config'))
CONFIG_FILE_PATH = path.join(CONFIG_DIR_PATH, 'config.yaml')
CONFIG_EXAMPLE_PATH = path.join(CONFIG_DIR_PATH, 'config.example.yaml')
logger.debug('The config file path is {}.'.format(CONFIG_FILE_PATH))


def get_config(config_path=None):
    """
    Return the config from a yaml file as a dictionary. Create one file if not existing, using example file as template.

    :param config_path:
    :return:
    """
    if config_path is None:
        try:
            with open(CONFIG_FILE_PATH, 'rb') as config_stream:
                config_dict = yaml.load(config_stream, Loader=Loader)
        except IOError:
            logger.info('')
            try:
                os.makedirs(CONFIG_DIR_PATH)
            except OSError as exc:
                if exc.errno == errno.EEXIST and path.isdir(CONFIG_DIR_PATH):
                    pass
                else:
                    raise
            with open(CONFIG_FILE_PATH, 'a'):
                os.utime(CONFIG_FILE_PATH, None)
            try:
                with open(CONFIG_EXAMPLE_PATH, 'rb') as config_example_stream:
                    config_dict_example = yaml.load(config_example_stream, Loader=Loader)
                # TODO : console based example file modification
                with open(CONFIG_FILE_PATH, 'wb') as config_stream:
                    yaml.dump(config_dict_example, config_stream, Dumper=Dumper, encoding='utf-8')
            except IOError:
                logger.critical("No example file. Exiting.")
                sys.exit(0)
            try:
                with open(CONFIG_FILE_PATH, 'rb') as config_stream:
                    config_dict = yaml.load(config_stream, Loader=Loader)
            except IOError:
                sys.exit(0)
    else:
        with open(config_path, 'rb') as config_stream:
            config_dict = yaml.load(config_stream, Loader=Loader)
    return config_dict
