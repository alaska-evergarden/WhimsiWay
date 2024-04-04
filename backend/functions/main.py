import logging
from firebase_functions import https_fn
from firebase_admin import initialize_app

from flask import Flask, request
from top5 import get_top_5
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/endpoint')
def endpoint():
    try:
        city = request.args.get('city', None)
        get_top_5(city)
        return "success"
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

@https_fn.on_request()
def collections_api(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("Hello world!")

if __name__ == '__main__':
    app.run(debug=True)