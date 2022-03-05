# from Ml_model import predict
import os
from dotenv import load_dotenv

load_dotenv()


def test_predict_severe_toxicity():
    severe_toxicity_1 = os.getenv('severe_toxicity_1')
    severe_toxicity_2 = os.getenv('severe_toxicity_2')
    severe_toxicity_3 = os.getenv('severe_toxicity_3')

    assert predict(severe_toxicity_1)['severe_toxicity'] > 0.5
    assert predict(severe_toxicity_2)['severe_toxicity'] > 0.5
    assert predict(severe_toxicity_3)['severe_toxicity'] > 0.5


def test_predict_obscene():
    obscene_1 = os.getenv('obscene_1')
    obscene_2 = os.getenv('obscene_2')
    obscene_3 = os.getenv('obscene_3')

    assert predict(obscene_1)['obscene'] > 0.9
    assert predict(obscene_2)['obscene'] > 0.9
    assert predict(obscene_3)['obscene'] > 0.9

def test_predict_threat():
    threat_1 = os.getenv('threat_1')
    threat_2 = os.getenv('threat_2')
    threat_3 = os.getenv('threat_3')

    assert predict(threat_1)['threat'] > 0.9
    assert predict(threat_2)['threat'] > 0.9
    assert predict(threat_3)['threat'] > 0.9

def test_predict_insult():
    insult_1 = os.getenv('insult_1')
    insult_2 = os.getenv('insult_2')
    insult_3 = os.getenv('insult_3')

    assert predict(insult_1)['insult'] > 0.9
    assert predict(insult_2)['insult'] > 0.9
    assert predict(insult_3)['insult'] > 0.9

def test_predict_identity_attack():
    identity_attack_1 = os.getenv('identity_attack_1')
    identity_attack_2 = os.getenv('identity_attack_2')
    identity_attack_3 = os.getenv('identity_attack_3')

    assert predict(identity_attack_1)['identity_attack'] > 0.9
    assert predict(identity_attack_2)['identity_attack'] > 0.9
    assert predict(identity_attack_3)['identity_attack'] > 0.9