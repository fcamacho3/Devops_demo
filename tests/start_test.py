from app import start


def test_app_start():
    '''Testing start function for application '''
    assert start() == True
