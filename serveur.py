#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
from flask import render_template

import random
import json
app = Flask(__name__, static_url_path='')

table = ""
# Fonction de réponse
@app.route("/")
def connexion():
  return app.send_static_file('inte.html')

# Requête R4 - Rejoindre une partie
@app.route("/players", methods=["POST"])
def addPlayer():
    data = request.get_json()
    if 'name' in data:
        table = "{\"name\": \""+data['name']+"\",\"infoPlayer\": {\"location\": [{\"latitude\": 25}, {\"longitude\": 50}],\"argent\": [{\"dispo\": 1.0}, {\"ventes\": 0.0$
    print table
    return json.dumps(table), 200, { "Content-Type": "application/json" }

# Requête R1/R7 - Metrology
@app.route("/metrology", methods=["GET", "POST"])
def metrology():
    global json_table
    if request.method == "GET":
        return "OK:GET_METROLOGY"
    elif request.method == "POST":
        return "OK:POST_METROLOGY"

    #return json.dumps(json_table), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
        app.run()
