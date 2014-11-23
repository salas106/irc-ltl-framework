import os
import os.path as path
import errno
import sys

import yaml


try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import utils.log

logger = utils.log.get_logger('config')

config_dir_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, path.pardir, 'config'))
config_file_path = path.join(config_dir_path, 'config.yaml')
config_example_path = path.join(config_dir_path, 'config.example.yaml')
logger.debug('The config file path is {}.'.format(config_file_path))


def get_config():
    try:
        with open(config_file_path, 'rb') as config_stream:
            config_dict = yaml.load(config_stream)
    except IOError:
        logger.info('')
        try:
            os.makedirs(config_dir_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and path.isdir(config_dir_path):
                pass
            else:
                raise
        with open(config_file_path, 'a'):
            os.utime(config_file_path, None)
        try:
            with open(config_example_path, 'rb') as config_example_stream:
                config_dict_example = yaml.load(config_example_stream)
            # TODO : console based example file modification
            with open(config_file_path, 'wb') as config_stream:
                yaml.dump(config_dict_example, config_stream)
        except IOError:
            logger.critical("No example file. Exiting.")
            sys.exit(0)
        try:
            with open(config_file_path, 'rb') as config_stream:
                config_dict = yaml.load(config_stream)
        except Exception:
            sys.exit(0)
    return config_dict