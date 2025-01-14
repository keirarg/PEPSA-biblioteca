from __future__ import print_function
from __main__ import app
from flask import request,session
from bd import obtener_conexion
import json
import sys
import funciones_auxiliares
import controlador_usuarios
        
@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        libro_json = request.json
        username = libro_json['username']
        password = libro_json['password']
        respuesta,code= controlador_usuarios.login_usuario(username, password)
        return json.dumps(respuesta, cls = funciones_auxiliares.Encoder), code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        libro_json = request.json
        username = libro_json['username']
        password = libro_json['password']
        perfil = libro_json['profile']
        respuesta,code= controlador_usuarios.alta_usuario(username, password, perfil)
        return json.dumps(respuesta, cls = funciones_auxiliares.Encoder), code
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code


@app.route("/logout",methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status":"OK"}),200
