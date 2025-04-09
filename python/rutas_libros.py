from flask import request, session, make_response
import json
from __main__ import app
import controlador_libros
from funciones_auxiliares import Encoder, sanitize_input, calculariva, prepare_response_extra_headers,validar_session_admin,validar_session_normal

@app.route("/libros",methods=["GET"])
def libros():
    if (validar_session_normal()):
        libros,code= controlador_libros.obtener_libros()
    else:
        libros={"status":"Forbidden"}   
        code=403
    response=make_response(json.dumps(libros, cls = Encoder),code)
    return response

@app.route("/libros/<id>",methods=["GET"])
def libro_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            libro,code = controlador_libros.obtener_libro_por_id(id)
        else:
            libro={"status":"Forbidden"}
            code=403
    else:
        libro={"status":"Bad parameters"}
        code=401
    response=make_response(json.dumps(libro, cls = Encoder),code)
    return response

@app.route("/libros",methods=["POST"])
def guardar_libro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        if "titulo" in request.json and "autor" in request.json and "foto" in request.json:
            titulo = sanitize_input(request.json["titulo"])
            autor = sanitize_input(request.json["autor"])
            anio = request.json["anio"]
            precio = request.json["precio"]
            if (request.json["foto"]):
                foto = sanitize_input(request.json["foto"])
            else:
                foto=""
            if isinstance(titulo,str) and isinstance(autor, str) and anio.isnumeric() and precio.isnumeric() and len(titulo)<255 and len(autor)<255 and len(foto)<255:
                if (validar_session_admin()):
                    precio=float(precio)
                    respuesta, code=controlador_libros.insertar_libro(titulo, autor, anio, precio, precio + calculariva(precio), foto)
                else:
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)  
    return response

@app.route("/libros/<id>", methods=["DELETE"])
def eliminar_libro(id):
    if(validar_session_admin()):
        respuesta,code=controlador_libros.eliminar_libro(id)
    else:
        respuesta={"status":"Forbidden"}
        code=403
    response=make_response(json.dumps(respuesta, cls=Encoder), code)
    return response
    
@app.route("/libros", methods=["PUT"])
def actualizar_libro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        if "id" in request.json and "titulo" in request.json and "autor" in request.json and"anio" in request.json and "precio" in request.json and "foto" in request.json:
            id = request.json["id"]
            titulo = sanitize_input(request.json["titulo"])
            autor = sanitize_input(request.json["autor"])
            anio = request.json["anio"]
            precio = request.json["precio"]
            if (request.json["foto"]):
                foto = sanitize_input(request.json["foto"])
            else:
                foto=""
            if id.isnumeric() and isinstance(titulo,str) and isinstance(autor, str) and anio.isnumeric() and precio.isnumeric() and isinstance(foto, str) and len(titulo)<255 and len(autor)<255 and len(foto)<255:
                id=int(id)
                anio=int(anio)
                precio=float(precio)
                if (validar_session_normal()):
                    respuesta, code=controlador_libros.actualizar_libro(id, titulo, autor, anio, precio, precio + calculariva(precio), foto)
                else:
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request1"}
                code=401
        else:
            respuesta={"status":"Bad request2"}
            code=401
    else:
        respuesta={"status":"Bad request3"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response