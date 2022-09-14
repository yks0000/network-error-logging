import json
import logging
import os
import random

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from rich.console import Console

console = Console()

FORMAT = "'%(asctime)s api=%(name)s.%(funcName)s [%(levelname)-7s]: %(message)s'"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]")
NEL_ENDPOINT = os.environ.get('NEL_ENDPOINT', "https://de34-49-207-197-21.in.ngrok.io/nel/report")

app = Flask(__name__)
cors = CORS(app=app,
            origins='*',
            methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
            allow_headers=['Access-Control-Allow-Origin',
                           'Access-Control-Allow-Methods',
                           'Access-Control-Allow-Headers',
                           'Content-Type',
                           'Authorization'])


@app.route('/test')
@cross_origin(cors)
def client_path():  # put application's code here
    name = request.args.get("name")
    if name:
        res_msg = f'Hello {name}'
    else:
        res_msg = f'Hello World'
    response = make_response(jsonify(message=res_msg), 200)
    response.headers["nel"] = json.dumps({
        "report_to": "network-errors",
        "max_age": 2592000,
        "include_subdomains": True
    }
    )
    response.headers["report-to"] = json.dumps({
        "group": "network-errors",
        "max_age": 2592000,
        "include_subdomains": True,
        "endpoints": [{"url": NEL_ENDPOINT}]
    })
    return response


@app.route('/error')
@cross_origin(cors)
def error_path():  # put application's code here
    status = random.choice([400, 401, 403, 500, 502, 504])
    response = make_response(jsonify(message=f"status is {status}"), status)
    response.headers["nel"] = json.dumps({
        "report_to": "network-errors",
        "max_age": 2592000,
        "include_subdomains": True
    }
    )
    response.headers["report-to"] = json.dumps({
        "group": "network-errors",
        "max_age": 2592000,
        "include_subdomains": True,
        "endpoints": [{"url": NEL_ENDPOINT}]
    })
    return response


if __name__ == '__main__':
    app.run(port=8000)
