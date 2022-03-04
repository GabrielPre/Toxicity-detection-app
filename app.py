from flask import Flask, request
from Ml_model import predict, generate_model
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram

start_http_server(8010)
app = Flask(__name__)

REQUESTS = Counter('hello_worlds_total', 'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')
INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in progress.')
LAST = Gauge('hello_world_last_time_seconds', 'The last time a Hello World was served.')
LATENCY = Summary('hello_world_latency_seconds', 'Time for a request Hello World.')

def get_hit_count():
    retries= 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc :
            if retries == 0 :
                raise exc
            retries -=1
            time.sleep(0.5)
            
@app.route('/metrics')
def hello():
    start = time.time()
    REQUESTS.inc()
    INPROGRESS.inc()
    LAST.set(start)

    time.sleep(random.random())
    with EXCEPTIONS.count_exceptions(): 
        # Une chance sur deux
        if random.choice((True, False)):
            INPROGRESS.dec()
            LATENCY.observe(time.time() - start)
            return "hello to my sample flask app, I have been seen {} times \n".format(get_hit_count())

        INPROGRESS.dec()
        LATENCY.observe(time.time() - start)
        raise Exception()


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
    generate_model()