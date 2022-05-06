# app.py
from flask import Flask, request, jsonify
from numpy import sqrt

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


def _find_next_id():
    return max(country["id"] for country in countries) + 1


# @app.route("/countries", methods=["GET"])
@app.get("/countries")
def get_countries():
    return jsonify(countries)


#
# @app.route("/countries", methods=["POST"])
@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


@app.post("/calculation")
def calculation_dummy():
    if request.is_json:
        data = request.get_json()
        result = sqrt(data['A']) + data['B']**2
        return {"C": result}, 201
    return {"error": "Request must be JSON"}, 415


