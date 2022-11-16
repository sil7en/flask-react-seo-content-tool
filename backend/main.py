import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/keywords")
def keywords():
    return {"keywords": ["keyword 1","keyword 2","keyword 3"]}

if __name__ == '__main__':
    app.run(debug=True)