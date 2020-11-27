#Importaremos los modulos para que descargamos
#Primero vamos a importar los modulos de Flask
from flask import Flask, render_template, request

#Ahora vamos a importar nuestro Chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import logging 

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

"""NOTA: para este punto del desarrollo con respecto a la creacion de las rutas, la API, entre otras cosas
ya no se comentaran, en primer lugar me da hueva y en segundo el codigo es mas comentario que codigo, si quieres saber para que sirve
las lineas que no tengan comentarios, checa mis otros repositorios, te lo juro por la virgen que esta comentado y explicado"""

app = Flask(__name__)

#Craremos el ChatBot
#Ah la configuracion del Chatbot como el anterior le mandaremos algunos atributos
Edward = ChatBot('Edward', storage_adapter="chatterbot.storage.SQLStorageAdapter")
#Crearemos al entrenador (para que nuestro Bot funcione)
Entrenador = ChatterBotCorpusTrainer(Edward)
#Daremos el idioma (para el proyecto usaremos Español ;) )
Entrenador.train('chatterbot.corpus.spanish') 
Entrenador.train("data/data.yml")

#Creacion de la ruta inicial
@app.route('/')
def inicio():
    return render_template('index.html')

#Ruta para recibir las respuestas
@app.route('/chat')
def chat():
    #Variable para el ingreso de texto por el usuario
    IngresoUsu = request.args.get("msg")
    #Retornamos los mensajes del usuario
    return str(Edward.get_response(IngresoUsu))


if __name__ == "__main__":
    app.run(port = 8089, debug = True)