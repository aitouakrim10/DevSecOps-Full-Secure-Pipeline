from flask import Flask
import time
import datetime
from prometheus_client import start_http_server, Counter, Histogram

# prometheus metrics
PAGE_VISITS = Counter('page_visits_total', 'Number of visits')
TIMEZONE_CHECKS = Counter('timezone_checks_total', 'Number of timezone checks performed')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds')

app = Flask(__name__)

@app.route('/')
def home():
    with REQUEST_LATENCY.time():
        PAGE_VISITS.inc()
        TIMEZONE_CHECKS.inc()

        # timezone logic - prefer timezone-aware approach
        local_tz = datetime.datetime.now(datetime.timezone.utc).astimezone()
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        offset = -time.timezone if time.localtime().tm_isdst == 0 else -time.altzone
        offset_hrs = offset / 3600.0

        return f"""<html>
        <head><title>DevSecOps Demo</title></head>
        <body>
        <h1>Timezone Information</h1>
        <p>Local Timezone: {local_tz}</p>
        <p>Current Time: {current_time}</p>
        <p>UTC Offset: {offset_hrs:+.1f} hours</p>
        </body></html>
        """

@app.route('/healthz')
def health():
    return 'OK', 200

if __name__ == '__main__':
    # expose prometheus metrics on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', debug=False, port=5000)
