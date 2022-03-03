from detoxify import Detoxify 

detox_model = None

def generate_model():
    global detox_model
    detox_model = Detoxify('original')

def predict(inputmessage):
    if detox_model is None:
        generate_model()
    
    results = detox_model.predict(inputmessage)
    return results

if __name__ == '__main__':
    generate_model()