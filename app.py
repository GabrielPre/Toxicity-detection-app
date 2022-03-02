from flask import Flask, request
from Ml_model import predict
app = Flask(__name__)


with open('frontend.html') as f:
    frontend_template = f.read()

@app.route('/')
def index():
    return frontend_template


@app.route('/classify', methods=['GET'])
def classify():
    inputmessage = request.args.get('inputmessage')
    result = predict(inputmessage)

    result = { k: float(v) for k, v in result.items() }

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
