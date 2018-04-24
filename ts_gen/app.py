import time
import random

import numpy as np

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/tmeseries', methods=['GET'])
def get_timeseries():
    temp = 75 + (2 * np.random.rand() - 1)
    volt = 17 + (3 * np.random.rand() - 1)
    # a = json.dumps({"time": time.time(), "temp": temp, "volt": volt})
    return jsonify({"time": time.time(), "temp": temp, "volt": volt})

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8000,
            debug=True)