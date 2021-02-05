#!flask/bin/python
#-*- coding_ UTF-8 -*-

from flask import Flask,jsonify, Request,abort
from flask.wrappers import Request
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property



app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del Curriculum Vitae de German Rodriguez",
        "acciones" :  [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)


@app.route('/curriculum', methods=['GET'])
def cv():
    #url_imagen = Request.host_url + "fotoGer.jpg"
    cv = {
        "nombre" : "German",
        "apellido" : "Rodriguez",
        "residencia" : "Argentina",
        "experiencia" :  [{
            "posicion" : "< Describe Posicion >",
            "Empresa"  : "< nombre de empresa  >",
            "desde" : "< Cuando empezaste a trabajar >",
            "hasta" : "< Si no trabajas mas, desde cuando >",
            "Descripcion" : "< Detalle >"
        }],
        "Educacion" : {
            "nivel" : "< Nivel de estudio >",
            "titulo"  : "< Nombre de la carrera  >",
            "institucion" : "< donde estudiaste >",
            "Facultad" : "< Si no trabajas mas, desde cuando >",
            "Descripcion" : "< Mas Detalles >"
        },
        "Intereses" : ["python"  ,"apis","enseñar"],
        "redes" : {
            "github" : "https://github.com/DeveloperGER"
    
        },
     #   "foto" : url_imagen
    }
    return jsonify(cv)

@app.route('/mensajes', methods=['POST'] ) 
def contacto():
    mensaje = Request.get_data()


    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST. ")
    print("MENSAJE DE CONTACTO: " + str(mensaje))
    
    
    return "Gracias por su mensaje"  

if __name__ == '__main__':
    app.run()
