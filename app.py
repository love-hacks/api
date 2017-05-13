# coding=utf-8
import requests
from flask import Flask, jsonify


app = Flask(__name__)
url = 'https://api.sde.globo.com/atletas/'
headers = {'token': 'hack2017-grupo1'}
athlete =  {
"name" : None,
"weight" : 0,
"photo" : None,
"height" : 0,
"kmPerHour" : 0
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
    #Neymar
    if id == "63007":
        print "entrou"
        response_api = requests.get(url + id, headers=headers).json()
        result_api = response_api["resultados"]
        athlete["photo"] = result_api["fotos"]["300x300"]
        athlete["name"] = result_api["nome"]
        athlete["weight"] = result_api["peso"]
        athlete["height"] = result_api["altura"]
        athlete["kmPerHour"] = 34.83
        print "saiu"
    #Messi
    elif id == "1":
        athlete["photo"] = "http://www.alagoas24horas.com.br/wp-content/uploads/2017/01/Messi.jpg"
        athlete["name"] = "Lionel Andrés Messi"
        athlete["weight"] = 72
        athlete["height"] = 1.7
        athlete["kmPerHour"] = 32.27
    elif id == "2":
        athlete["photo"] = "http://www.alagoas24horas.com.br/wp-content/uploads/2017/01/Messi.jpg"
        athlete["name"] = "Andrés Iniesta Luján"
        athlete["weight"] = 68
        athlete["height"] = 1.7
        athlete["kmPerHour"] = 31.62
    elif id == "3":
        #33,52
        athlete["photo"] = "http://www.alagoas24horas.com.br/wp-content/uploads/2017/01/Messi.jpg"
        athlete["name"] = "Gerard Piqué Bernabéu"
        athlete["weight"] = 85
        athlete["height"] = 1.9
        athlete["kmPerHour"] = 33.52
    else:
        return jsonify([])
    print athlete
    return jsonify(athlete)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
