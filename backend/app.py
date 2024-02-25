from flask import Flask, request
from top5 import get_top_5
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/endpoint')
def endpoint():
    city = request.args.get('city', None)
    get_top_5(city)
    return "success"


if __name__ == '__main__':
    app.run(debug=True)