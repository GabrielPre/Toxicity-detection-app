from flask.testing import FlaskClient
from time import time
from app import app


test_app: FlaskClient

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    global test_app
    app.testing = True
    test_app = app.test_client()

def predict(text):
    return test_app.get(f'classify?inputmessage=${text}').json

def test_response():
    """
    Assert the server can handle 100 requests in less than a minute
    """

    start = time()

    for i in range(50):
        print('Iteration', i)
        test_app.get(f'classify?inputmessage="oh hi"').json
        test_app.get(f'classify?inputmessage="i hate you"').json

    end = time()

    diff = end - start
    assert diff < 60
    print('Ran 100 requests in', diff, 'seconds')