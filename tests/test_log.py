import utils.log

import os


def test_log_in_default_log_file():
    log_path = os.path.abspath(os.path.join(os.sep, os.path.dirname(__file__), os.path.pardir, 'logs', 'test.log'))
    if os.path.exists(log_path):
        os.remove(log_path)
    logger = utils.log.get_logger('test')
    logger.debug("Im testing right now")
    assert os.path.exists(log_path)
    os.remove(log_path)


def test_log_in_specified_log_file():
    log_path = os.path.abspath(os.path.join(os.sep, os.path.dirname(__file__), os.path.pardir, 'logs', 'test1.log'))
    if os.path.exists(log_path):
        os.remove(log_path)
    logger = utils.log.get_logger('test1', log_path=log_path)
    logger.debug("Im testing right now")
    assert os.path.exists(log_path)
    os.remove(log_path)


def test_log_in_specified_log_file_dir_not_existing():
    log_path = os.path.abspath(os.path.join(os.sep, os.path.expanduser("~"), '.botIrc', 'logs', 'test.log'))
    if os.path.exists(log_path):
        os.remove(log_path)
    logger = utils.log.get_logger('test1', log_path=log_path)
    logger.debug("Im testing right now")
    assert os.path.exists(log_path)
    os.remove(log_path)


def test_log_in_specified_log_file_no_access():
    log_path = os.path.abspath(os.path.join(os.sep, os.path.abspath(os.sep), 'run', 'logs', 'test.log'))
    if os.path.exists(log_path):
        os.remove(log_path)
    logger = utils.log.get_logger('test1', log_path=log_path)
    logger.debug("Im testing right now")
    assert not os.path.exists(log_path)