import json
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import os
from dotenv import load_dotenv
from app import appMain

# init Flask
app = Flask(__name__)

# init dotenv to  use variables from .env file
load_dotenv()

# define project_path
project_path = os.getenv('PATH_PROJECT_FOLDER')

def load_json_data():
    global keywords_data
    global keywords
    with open('data.json', 'r') as f:
        keywords = json.load(f)
        keywords_data = keywords

load_json_data()

def write_changes_to_file():
    global data
    data = {k: v for k, v in keywords.items()}
    with open('data.json', 'w') as f:
        json.dump(data, f)
        

write_changes_to_file()

@app.route("/")
def home():
    return {'api': 'seo-content-tool'}

@app.route("/keywords")
def keywords():
    return keywords_data

@app.route("/keywords/<keyword>")
def keyword(keyword):
    obj_return = appMain(keyword)
    return obj_return  

if __name__ == '__main__':
    app.run(debug=True)