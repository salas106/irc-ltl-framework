# -*- coding: utf8 -*-

__author__ = 'Salas'
__copyright__ = 'Copyright 2014 LTL'
__credits__ = ['Salas']
__license__ = 'MIT'
__version__ = '0.2.0'
__maintainer__ = 'Salas'
__email__ = 'Salas.106.212@gmail.com'
__status__ = 'Pre-Alpha'

from nose.tools import raises
import utils.config


@raises(IOError)
def test_config_wrong_path_raise_exception():
    utils.config.get_config('./some/path/not/existing')


def test_config_right_path_return_dict():
    assert isinstance(utils.config.get_config(), dict)
