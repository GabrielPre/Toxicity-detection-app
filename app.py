from flask import Flask, request
from Ml_model import predict, generate_model
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram
import time

start_http_server(8010)
app = Flask(__name__)

REQUESTS = Counter('detoxify_total', 'Hello Worlds requested.')
EXCEPTIONS = Counter('detoxify_exceptions_total', 'Exceptions serving Hello World.')
INPROGRESS = Gauge('detoxify_inprogress', 'Number of Hello Worlds in progress.')
LAST = Gauge('detoxify_last_time_seconds', 'The last time a Hello World was served.')
LATENCY = Summary('detoxify_latency_seconds', 'Time for a request Hello World.')


with open('frontend.html') as f:
    frontend_template = f.read()

@app.route('/')
def index():
    return frontend_template


@app.route('/classify', methods=['GET'])
def classify():
    REQUESTS.inc()
    INPROGRESS.inc()

    start = time.time()

    inputmessage = request.args.get('inputmessage')
    result = predict(inputmessage)
    result = { k: float(v) for k, v in result.items() }

    LATENCY.observe(time.time() - start)
    LAST.set(time.time())

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    generate_model()