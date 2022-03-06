from flask import json
from flask.testing import FlaskClient

from app import app
from encoder_decoder import decode

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
    assert type(response['severe_toxicity']) == float
    assert type(response['obscene']) == float
    assert type(response['threat']) == float
    assert type(response['insult']) == float
    assert type(response['identity_attack']) == float
    
def test_positive():
    """
    Assert the server correctly classifies positive sentences
    """
    assert predict('oh hi')['toxicity'] < 0.1
    assert predict('i like you')['toxicity'] < 0.1
    assert predict('thanks!')['toxicity'] < 0.1


def test_predict_severe_toxicity():
    severe_toxicity_1 = b'c21lbGx5IGZhdCBtb3RoZXIgZnVja2Vy'
    severe_toxicity_2 = b'cmV0YXJkZWQgY29jayBzdWNraW5nIGJpdGNo'
    severe_toxicity_3 = b'R2V0IGZ1Y2tlZCBmYXQgY3VudA=='

    assert predict(decode(severe_toxicity_1))['severe_toxicity'] > 0.5
    assert predict(decode(severe_toxicity_2))['severe_toxicity'] > 0.5
    assert predict(decode(severe_toxicity_3))['severe_toxicity'] > 0.5


def test_predict_obscene():
    obscene_1 = b'RnVjayB5b3U='
    obscene_2 = b'SSdsbCBlbmQgeW91IGN1bnQ='
    obscene_3 = b'Qml0Y2g='

    assert predict(decode(obscene_1))['obscene'] > 0.8
    assert predict(decode(obscene_2))['obscene'] > 0.8
    assert predict(decode(obscene_3))['obscene'] > 0.8

def test_predict_threat():
    threat_1 = b'SSdsbCBlbmQgeW91'
    threat_2 = b'eW91IHNob3VsZCBraWxsIHlvdXJzZWxm'
    threat_3 = b'SSBhbSBnb2luZyB0byByYXBlIHlvdXIgbW9t'

    assert predict(decode(threat_1))['threat'] > 0.5
    assert predict(decode(threat_2))['threat'] > 0.8
    assert predict(decode(threat_3))['threat'] > 0.8

def test_predict_insult():
    insult_1 = b'cmV0YXJk'
    insult_2 = b'cmV0YXJkZWQgZnVjaw=='
    insult_3 = b'Qml0Y2g='

    assert predict(decode(insult_1))['insult'] > 0.8
    assert predict(decode(insult_2))['insult'] > 0.8
    assert predict(decode(insult_3))['insult'] > 0.8

def test_predict_identity_attack():
    identity_attack_1 = b'S2lsbCBhbGwgamV3cw=='
    identity_attack_2 = b'ZHVtYiBuaWdnZXJz'
    identity_attack_3 = b'cmV0YXJkZWQgZ2F5IHNoaXQ='

    assert predict(decode(identity_attack_1))['identity_attack'] > 0.8
    assert predict(decode(identity_attack_2))['identity_attack'] > 0.8
    assert predict(decode(identity_attack_3))['identity_attack'] > 0.8