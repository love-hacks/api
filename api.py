import requests
from flask import Flask, Response, jsonify


app = Flask(__name__)
url = 'https://api.sde.globo.com/atletas/'
headers = {'token': 'hack2017'}

@app.route("/")
def index():
    response = [
        {"status": 404, "code": 404, "description": "Invalid parameter(s): Status id"}
    ]
    return jsonify(results=response)

@app.route("/api/v1/athlete/<id>", methods=['GET'])
def getAthlete(id):
    response = [
        {"status": 200, "code": 200, "description": id}
    ]
    response_api = requests.get(url, headers=headers).json()
    print response_api['resultados']
    return jsonify(results=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
