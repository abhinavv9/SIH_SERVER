from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route("/")
def hello_world():
    return "{'success': 'true', 'message': 'wrong route'}"

app.run( debug = True)

import csv, json

csv_file = './data.csv'
json_file = './data.json'

data = {}
with open(csv_file) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        id = row['Domain']
        data[id] = row

with open(json_file, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

@app.route('/sumarize')
def summarize():
    return data