from nose.tools import raises
import utils.config


@raises(IOError)
def config_wrong_path_raise_exception():
    utils.config.get_config('./some/path/not/existing')


def config_right_path_return_dict():
    assert isinstance(utils.config.get_config(), dict)