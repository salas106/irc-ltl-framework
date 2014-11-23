import os

import logging
from logging.handlers import RotatingFileHandler
import coloredlogs

log_dir_path = os.path.abspath(os.path.join(os.sep, os.path.pardir(os.path.dirname(__file__)), 'config'))


def get_logger(name):
    logger = logging.getLogger(name)
    # File logging
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    log_file_path = os.path.abspath(os.path.join(log_dir_path, '{}.log'.format(name)))
    file_handler = RotatingFileHandler(log_file_path, 'a', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # Console logging
    steam_handler = coloredlogs.ColoredStreamHandler()
    formatter = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
    steam_handler.setLevel(logging.DEBUG)
    steam_handler.setFormatter(formatter)
    logger.addHandler(steam_handler)
    return logger