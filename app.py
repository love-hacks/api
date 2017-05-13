import requests
from flask import Flask, jsonify


app = Flask(__name__)
url = 'https://api.sde.globo.com/atletas/'
headers = {'token': 'hack2017-grupo1'}
athlete =  {
"name" : None,
"weight" : 0,
"photo" : None,
"height" : 0
}

@app.route("/")
def index():
    response = [
        {"status": 404, "code": 404, "description": "Resource not found"}
    ]
    return jsonify(response)

@app.route("/api/v1/athlete/")
def athleteIndex():
    response = [
        {"status": 404, "code": 404, "description": "Invalid parameter(s): Athlete id is required"}
    ]
    return jsonify(response)

@app.route("/api/v1/athlete/<id>", methods=['GET'])
def getAthlete(id):
    response = [
        {"status": 200, "code": 200, "description": id}
    ]
    response_api = requests.get(url + id, headers=headers).json()
    result_api = response_api["resultados"]
    athlete["photo"] = result_api["fotos"]["300x300"]
    athlete["name"] = result_api["nome"]
    athlete["weight"] = result_api["peso"]
    athlete["height"] = result_api["altura"]
    print athlete
    return jsonify(athlete)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
