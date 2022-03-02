from flask import json
from flask.testing import FlaskClient

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
    Assert the server responds with a 200 status
    """
    assert test_app.get(f'classify?inputmessage=any').status_code == 200


def test_format():
    """
    Assert the server responds with a string
    """
    response = predict('oh hi')

    assert type(response) == dict
    assert type(response['toxicity']) == float
    
def test_positive():
    """
    Assert the server correctly classifies positive sentences
    """
    assert predict('oh hi')['toxicity'] < 0.1