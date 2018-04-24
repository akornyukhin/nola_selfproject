import requests
import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    while True:
        a = requests.get('http://localhost:8000/api/tmeseries').json()
        print(a)
        time.sleep(1.0)
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8082,
            debug=True)