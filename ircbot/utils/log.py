import os
import os.path as path

import logging
from logging.handlers import RotatingFileHandler
import coloredlogs

log_dir_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, path.pardir, 'logs'))


def get_logger(name):
    logger = logging.getLogger(name)
    # File logging
    logger.setLevel(logging.DEBUG)
    formatter_file = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    log_file_path = path.join(log_dir_path, '{}.log'.format(name))
    try:
        with open(log_file_path):
            pass
    except IOError:
        with open(log_file_path, 'a'):
            os.utime(log_file_path, None)

    file_handler = RotatingFileHandler(log_file_path, 'a', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_file)
    logger.addHandler(file_handler)
    # Console logging
    steam_handler = coloredlogs.ColoredStreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    logger.addHandler(steam_handler)
    return logger