from nose.tools import raises


@raises(IOError)
def test_me():
    with open('/test/me/not/') as test:
        pass