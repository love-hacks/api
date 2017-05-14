# coding=utf-8
import requests
from flask import Flask, jsonify, request,  render_template

app = Flask(__name__)
url = 'https://api.sde.globo.com/atletas/'
headers = {'token': 'hack2017-grupo1'}


def getIniesta():
    athlete = {}
    athlete["id"] = 2
    athlete["photo"] = "http://images.performgroup.com/di/library/GOAL_INTERNATIONAL/11/a1/uefa-team-of-the-year-andres-iniesta_180syh14bzf51sks6lb2qvyvb.jpg?t=-2017137824&w=620&h=430"
    athlete["name"] = "Andrés Iniesta Luján"
    athlete["weight"] = 68
    athlete["height"] = 1.7
    athlete["kmPerHour"] = 31.62
    return athlete

def getMessi():
    athlete = {}
    athlete["id"] = 1
    athlete["photo"] = "http://www.alagoas24horas.com.br/wp-content/uploads/2017/01/Messi.jpg"
    athlete["name"] = "Lionel Andrés Messi"
    athlete["weight"] = 72
    athlete["height"] = 1.7
    athlete["kmPerHour"] = 32.27
    return athlete

def getPique():
    athlete = {}
    athlete["id"] = 3
    athlete["photo"] = "http://s.weltsport.net/bilder/spieler/gross/27798.jpg"
    athlete["name"] = "Gerard Piqué Bernabéu"
    athlete["weight"] = 85
    athlete["height"] = 1.9
    athlete["kmPerHour"] = 33.52
    return athlete

def getNeymar():
    athlete = {}
    response_api = requests.get(url + "63007", headers=headers).json()
    result_api = response_api["resultados"]
    athlete["id"] = 63007
    athlete["photo"] = result_api["fotos"]["300x300"]
    athlete["name"] = result_api["nome"]
    athlete["weight"] = result_api["peso"]
    athlete["height"] = result_api["altura"]
    athlete["kmPerHour"] = 34.83
    return athlete

@app.errorhandler(404)
def not_found(e):
    response = {"status": "Not found", "code": 404, "description": "Resource not found"}
    return jsonify(response), 404

@app.route("/api/v1/athletes/")
def getAthletes():
    athlete_list = []
    athlete_list.append(getIniesta())
    athlete_list.append(getPique())
    athlete_list.append(getNeymar())
    athlete_list.append(getMessi())
    return jsonify(athlete_list)

@app.route("/api/v1/athletes/<id>", methods=['GET'])
def getAthlete(id):
    #Make HTTP Request
    if id == "63007":
        return jsonify(getNeymar())
    elif id == "1":
        return jsonify(getMessi())
    elif id == "2":
        return jsonify(getIniesta())
    elif id == "3":
        return jsonify(getPique())
    else:
        return jsonify([])

@app.route("/api/v1/athletes/races", methods=['GET'])
def getRacesByAttributes():
    distance = request.args.get("distance")
    speed = request.args.get("speed")
    print speed
    time = request.args.get("time")

    if (speed and distance) or (not speed and not distance):
        error_message = {"status": "Bad request", "code": 400, "description": "Invalid options!"}
        return jsonify(error_message)
    if (distance and not time):
        error_message = {"status": "Bad request", "code": 400, "description": "Invalid parameter(s): Distance and time are required"}
        return jsonify(error_message)
    
    result = {
        "previous" : None,
        "next" : None
    }

    if distance:
        print "entru em em distance"
        pique_distance = 33.52*time
        iniesta_distance = 31.62*time
        messi_distance = 32.27*time
        neymar_distance = 34.83*time
        if distance < iniesta_distance:
            result["previous"] = {}
            result["next"] = getIniesta()
        elif iniesta_distance <= distance < messi_distance:
            result["previous"] = getIniesta()
            result["next"] = getMessi()
        elif messi_distance <= distance < pique_distance:
            result["previous"] = getMessi()
            result["next"] = getPique()
        elif pique_distance <= distance < neymar_distance:
            result["previous"] = getPique()
            result["next"] = getNeymar()
        elif distance >= neymar_distance:
            result["previous"] = getNeymar()
            result["next"] = {}
    else:
        print "entrou em speed"
        print
        if float(speed) < 31.62:
            print "1"
            result["previous"] = {}
            result["next"] = getIniesta()
        elif 31.62 <= speed < 32.27:
            print "2"
            result["previous"] = getIniesta()
            result["next"] = getMessi()
        elif float(32.27) <= speed < 33.52:
            print "3"
            result["previous"] = getMessi()
            result["next"] = getPique()
        elif 33.52 <= float(speed) < 34:
            print "4"
            result["previous"] = getPique()
            result["next"] = getNeymar()
        elif speed >= 34:
            print "5"
            result["previous"] = getNeymar()
            result["next"] = {}

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
