from detoxify import Detoxify 

detox_model = Detoxify('original')

def predict(inputmessage):
    results = detox_model.predict(inputmessage)
    return results