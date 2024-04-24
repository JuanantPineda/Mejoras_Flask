from flask import Flask, render_template, abort, redirect,request
app = Flask(__name__)	
import os

import json
with open("estructura.json") as fichero:
    datos=json.load(fichero)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/formulario',methods=["POST"])
def episodios():
    cadena=request.form.get("letra")
    temporada=request.form.get("temporada")
    
    episodios = []
    finalEpisodios = []

    for var in datos["_embedded"]["episodes"]:
        diccionario = {"nombre": var["name"], "puntuacion": var["rating"]["average"],"temporada": var["season"],"id": var["id"]}
        episodios.append(diccionario)
    
    if int(temporada) == 0:
        for var in episodios:
            if var["nombre"].startswith(cadena):
                diccionario2 = {"nombre": var["nombre"], "puntuacion": var["puntuacion"],"temporada": var["temporada"],"id":var["id"]}
                finalEpisodios.append(diccionario2)
    else:
        for var in episodios:
            if var["nombre"].startswith(cadena):
                if int(temporada) == var["temporada"]:
                    diccionario2 = {"nombre": var["nombre"], "puntuacion": var["puntuacion"],"temporada": var["temporada"],"id":var["id"]}
                    finalEpisodios.append(diccionario2)
            
    return render_template("formulario.html",finalEpisodios=finalEpisodios)

@app.route('/detalle/<id>')
def detalle(id):
    detalles = []
    for var in datos["_embedded"]["episodes"]:
        if int(id) == var["id"]:
            diccionario = {"nombre": var["name"],"temporada": var["season"],"episodio": var["number"],"emision": var["airdate"],"puntuacion": var["rating"]["average"]}
            detalles.append(diccionario)
            
    return render_template("detalle.html",id=id,detalles=detalles)

port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=False)