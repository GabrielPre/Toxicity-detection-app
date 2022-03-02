from Ml_model import predict

def test_positive_sentence():
    assert predict('oh hi')['toxicity'] < 0.1