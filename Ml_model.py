from unittest import result
from detoxify import Detoxify 

def predict(inputmessage):
    results = Detoxify('original').predict(inputmessage)
    return results