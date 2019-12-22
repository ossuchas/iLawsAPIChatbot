from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from ma import ma

app = Flask(__name__)

api = Api(app, prefix="/api/v1")
CORS(app, resources=r"/api/*", allow_headers="Content-Type")

load_dotenv(".env", verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTING")


@app.route('/')
def hello_world():
    return 'iLaw Chatbot Hello World 1.0.0..!!'


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
