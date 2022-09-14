import json
import logging

from flask import Flask, request
from rich.console import Console
from flask_cors import CORS, cross_origin

FORMAT = "'%(asctime)s api=%(name)s.%(funcName)s [%(levelname)-7s]: %(message)s'"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]")

console = Console()

app = Flask(__name__)
cors = CORS(app=app,
            origins='*',
            methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
            allow_headers=['Access-Control-Allow-Origin',
                           'Access-Control-Allow-Methods',
                           'Access-Control-Allow-Headers',
                           'Content-Type',
                           'Authorization'])


@app.route('/nel/report', methods=['POST'])
@cross_origin(cors)
def nel_events():  # put application's code here
    try:
        console.print_json(json.dumps(request.json))
        logging.info(f"Inside NEL: {request.headers}")
        return 'Hello World!'
    except Exception as error:
        logging.error(str(error))
        return 'Hello World!'


if __name__ == '__main__':
    app.run(port=9000)
