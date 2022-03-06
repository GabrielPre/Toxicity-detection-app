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

def test_severe_toxicity():
    severe_toxicity_1 = b'gAAAAABiJNrnXW243JthxleTfr7qh0EeoIzqJN4n9QtT16ETDfLNh5USWO7dbZTRrQPlDa5SiFmsTQgkMHzbXgAbPyZL1NEn9SHZ7ngY-mMi8v3-yO9sLxo='
    severe_toxicity_2 = b'gAAAAABiJNrnXjPAJyjGegRV6lQdFcXcSGeXfYxpFP_ylWVM4f9GyD3EJMzLPDyIOyGLAk2v84_90CHe9O6ou7M0oqAXIoFVAO-pwUGsOSiEzkKjdPga-g8='
    severe_toxicity_3 = b'gAAAAABiJNrnVbVeWFhjwJ11j7jnOV0O7gEdMN0WFDppkcPiGzlkp4zxAeIoXw_wHHtN_L9bYOAYbfGJfTR7HQdD0Zh350OYyNqOd81pOpIEn2VJy1l1aHw='

    assert predict(decode(severe_toxicity_1))['severe_toxicity'] > 0.5
    assert predict(decode(severe_toxicity_2))['severe_toxicity'] > 0.5
    assert predict(decode(severe_toxicity_3))['severe_toxicity'] > 0.5

def test_predict_obscene():
    obscene_1 = b'gAAAAABiJNrncGQ-66jFL6XehP9HXTiC2pb-w37n3zrFtfU5YRU2V7_D4EtCGSKudcS2ogstJQtl0EbvBojhH4T7ARQiE__iYw=='
    obscene_2 = b'gAAAAABiJNrnUCkT71PLPFxfC4uCJIr9kvxP_WvqfvdKVO4vPryNS2YKZQWiADzAi3ybM3CixEr7Riz6CPtRL0fq76R2iXVNpDXjf2QupTT06FUmscZmbwk='
    obscene_3 = b'gAAAAABiJNrnV0OyPo7jJpHKn1lRrGlHJKIhfqEPvy-mjVaM9YPIyrmQLd2iR5pC_4sWVhDp-56DFazYiG5HszJKyFU5sNecvw=='

    assert predict(decode(obscene_1))['obscene'] > 0.9
    assert predict(decode(obscene_2))['obscene'] > 0.9
    assert predict(decode(obscene_3))['obscene'] > 0.9

def test_predict_threat():
    threat_1 = b'gAAAAABiJNrnKdSeKBX4Zi5VaFKyDI1jfC-x-CCbgBdNe3mD1B9xSGI3UtnUKgARfZC5LoE8KrRpAwXpUVcM0LxJ_5OGz-GC3Q=='
    threat_2 = b'gAAAAABiJNrnfK7ZdJmVH6K85Lkk0uhAviAI5cxYOvJWbwBC5Rqmh-CvJwNHTH4kNhjSIa3EFb79Dmp2f_teoZm2-oKRvMkDvlIrvnEhO4vZKrvFQkPCL1c='
    threat_3 = b'gAAAAABiJNrnQjY7zwo89ij9tuBAyNuqZPqqdRHueib1oDX0otOiT4WO0ACL-NMVpMu4E0un01qEnm0f3tvueGI0ndt-V7yqEmbiKx73BLsDZSS6dTJXdco='

    assert predict(decode(threat_1))['threat'] > 0.9
    assert predict(decode(threat_2))['threat'] > 0.9
    assert predict(decode(threat_3))['threat'] > 0.9

def test_predict_insult():
    insult_1 = b'gAAAAABiJNrncLhFf6Frb6oyQfB5f4-6Asq9OY33wWmVcHt52Lkmwd0s3h-CUX2GPQ0f3s4IC9ual605cfm_ZVQLkS7mOcCptg=='
    insult_2 = b'gAAAAABiJNrnp6OkjfpNkHDiXnIJ7MdkEbCCESxnqg02ZQOXbhQHmTEsF1zcu_tU9x34eH_26ph7XktwWxXacZZa6Y2yY5PkAA=='
    insult_3 = b'gAAAAABiJNrnCBo4uoaHWo1pmjrxzdk3XhgqbCZzHQnUGTBb2ml1bAlq5IFXOmQUJuoW3kKdoWGFKpI4LF25Fwe8rfiMIsE2xA=='

    assert predict(decode(insult_1))['insult'] > 0.9
    assert predict(decode(insult_2))['insult'] > 0.9
    assert predict(decode(insult_3))['insult'] > 0.9

def test_predict_identity_attack():
    identity_attack_1 = b'gAAAAABiJNrnVZznxmFqkkOWK82-mHy4OeM6VY9gsOm1TDe4ruk4-8vWip_kkqTD61D-0Ci6fg5rMW-YgobTpVz6rS2jHR6OgA=='
    identity_attack_2 = b'gAAAAABiJNrnUQms1Km1Uos8stZZJRSvFUxtB4riJv5g1P5ZyKfJKLmK4FTICeuJ0PhEsZlC6s8Tu0vnjQHtJhcMlglYQN2EtQ=='
    identity_attack_3 = b'gAAAAABiJNrnfsKMUC5I2xWhlOKQAWVsJUnYTau6zMnmtbss8Qqcu2b5hzJh5c0tRSFFmtudR2_DN9nqa31B-Mviam3_DWq3I33RBrD5r8xkVe5CcMkuDVs='

    assert predict(decode(identity_attack_1))['identity_attack'] > 0.9
    assert predict(decode(identity_attack_2))['identity_attack'] > 0.9
    assert predict(decode(identity_attack_3))['identity_attack'] > 0.9