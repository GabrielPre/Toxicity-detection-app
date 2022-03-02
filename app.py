from flask.wrappers import Request
from flask import Flask, request, jsonify
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
    return jsonify(format(predict(inputmessage)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
