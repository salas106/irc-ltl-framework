import os
import errno
import sys

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import utils.log
logger = utils.log.get_logger('config')

config_dir_path = os.path.abspath(os.path.join(os.sep, os.path.pardir(os.path.dirname(__file__)), 'config'))
config_file_path = os.path.abspath(os.path.join(config_dir_path, 'config.yaml'))
config_example_path = os.path.abspath(os.path.join(config_dir_path, 'config.example.yaml'))
logger.debug('The config file path is {}.'.format(config_file_path))


def config():
    try:
        with open(config_file_path, 'rb') as config_stream:
            config_dict = load(config_stream)
    except IOError:
        logger.info('')
        # mkdir -p
        try:
            os.makedirs(config_dir_path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(config_dir_path):
                pass
            else:
                raise
        with open(config_file_path, 'a'):
            os.utime(config_file_path, None)
        # TODO :TUTORIAL TO FILL OUT THE DICT
        try:
            with open(config_file_path, 'rb') as config_stream:
                config_dict = load(config_stream)
        except Exception:
            sys.exit()
    return config_dict