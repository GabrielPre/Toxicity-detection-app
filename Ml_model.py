from unittest import result
from detoxify import Detoxify 

def predict():
    results = Detoxify('original').predict('I hate you')
    return results