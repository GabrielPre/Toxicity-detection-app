from detoxify import Detoxify

def predict(text):
    "Predict the toxicity of a given text"
    results = Detoxify('original').predict(text)
    return results

def main():
    print('Hello world')

if __name__ == "__main__" :
    main()