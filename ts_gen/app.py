import time
import os

import numpy as np

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/timeseries', methods=['GET'])
def get_timeseries():
    temp = np.round(75 + (2 * np.random.rand() - 1), 2)
    volt = np.round(17 + (3 * np.random.rand() - 1), 2)
    return jsonify({'time': time.mktime(time.localtime()), 'temp': temp, 'volt': volt})

@app.route('/')
def index():
    return '!', 200

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    app.run(host='0.0.0.0',
            port=port,
            debug=True)