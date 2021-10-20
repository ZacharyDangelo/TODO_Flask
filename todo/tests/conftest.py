import pytest

from todo.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)

    # Establish Application context.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, gets executed for each test function

    :param app: Pytest Function
    :return: Flask app client
    """
    yield app.test_client()
