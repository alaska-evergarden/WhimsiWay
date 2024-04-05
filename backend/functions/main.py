import functions_framework

import flask
from top5 import get_top_5
from flask_cors import CORS

@functions_framework.http
def test(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return 'Hello world!'

@functions_framework.http
def whimsi_api(request: flask.Request) -> flask.typing.ResponseReturnValue:
    try:
        # Set CORS headers for the main request
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        city = request.args.get('city', None)
        map = get_top_5(city)
        return flask.Response(map, headers=headers)
    except Exception as e:
        print(f"An error occurred: {str(e)}")