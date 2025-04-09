from __main__ import app
from bd import obtener_conexion
from funciones_auxiliares import sanitize_input
import sys

def insertar_libro(titulo, autor, anio, precio, precioIVA, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO libros(titulo, autor, anio, precio, precioIVA, foto) VALUES (%s, %s, %s, %s, %s, %s)",
                      (titulo, autor, int(anio), float(precio), float(precioIVA), foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        app.logger.info("Excepcion al insertar un libro")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_libro_a_json(libro):
    d = {}
    d['id'] = libro[0]
    d['titulo'] = sanitize_input(libro[1])
    d['autor'] = sanitize_input(libro[2])
    d['anio'] = libro[3]
    d['precio'] = libro[4]
    d['precioIVA'] = libro[5]
    if (libro[6]):
        d['foto'] = sanitize_input(libro[6])
    else:
        d['foto'] = ""
    return d

def obtener_libros():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, titulo, autor, anio, precio, precioIVA, foto FROM libros")
            libros = cursor.fetchall()
            librosjson=[]
            if libros:
                for libro in libros:
                    librosjson.append(convertir_libro_a_json(libro))
        conexion.close()
        code=200
    except Exception as e:
        app.logger.info(f"Excepcion al obtener los libros {e}")
        librosjson=[]
        code=500
    return librosjson,code

def obtener_libro_por_id(id):
    librojson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, titulo, autor, anio, precio, precioIVA, foto FROM libros WHERE id = %s", (id,))
            libro = cursor.fetchone()
            if libro is not None:
                librojson = convertir_libro_a_json(libro)
        conexion.close()
        code=200
    except:
       app.logger.info("Excepcion al obtener un libro")
       code=500
    return librojson,code


def eliminar_libro(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM libros WHERE id = %s LIMIT 1", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar un libro")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_libro (id, titulo, autor, anio, precio, precioIVA, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE libros SET titulo = %s, autor = %s, anio = %s, precio = %s, precioIVA=%s, foto=%s WHERE id = %s",
                       (titulo, autor, anio, precio, precioIVA, foto, id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al actualizar un libro")
        ret = {"status": "Failure" }
        code=500
    return ret,code
