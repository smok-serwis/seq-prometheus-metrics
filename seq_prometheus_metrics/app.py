import threading

import flask
from satella.coding.structures import Singleton
from werkzeug import run_simple

app = flask.Flask(__name__)


@Singleton
class MetricData:
    def __init__(self):
        self.data = {}

    def update_data(self, new_data):
        self.data = new_data


@app.route('/metrics')
def get_metrics():
    data = []
    for key, value in MetricData().data.items():
        data.append('%s{} %s' % (key, value))
    data.append('')
    return '\n'.join(data)


class WorkerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

    def run(self):
        run_simple('0.0.0.0', 80, app, threaded=True, use_reloader=False)
