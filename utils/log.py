import os
import os.path as path

import logging
from logging.handlers import RotatingFileHandler
import coloredlogs


def get_logger(name, log_path=None):
    logger = logging.getLogger(name)
    # File logging
    logger.setLevel(logging.DEBUG)
    formatter_file = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    if log_path is None:
        log_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, 'logs', '{}.log'.format(name)))
    else:
        log_dir_path = path.dirname(log_path)
        if not os.path.exists(log_dir_path):
            try:
                os.makedirs(log_dir_path)
            except PermissionError:
                print("No permission to write log file their")
                log_path = None
            except OSError:
                raise
            else:
                with open(log_path, 'a'):
                    os.utime(log_path, None)
    if log_path is not None:
        try:
            with open(log_path):
                pass
        except IOError:
            try:
                with open(log_path, 'a'):
                    os.utime(log_path, None)
            except IOError:
                raise
        file_handler = RotatingFileHandler(log_path, 'a', 1000000, 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter_file)
        logger.addHandler(file_handler)
    # Console logging
    steam_handler = coloredlogs.ColoredStreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    logger.addHandler(steam_handler)
    return logger