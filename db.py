import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='eventos'
)


#FUNCIONES DE USUARIO
#---------Registro de usuarios
def registrar_usuario(nombre, correo, clave, foto_perfil, rol_id):
    cursor = database.cursor()
    insert_query = "INSERT INTO usuarios (nombre, correo, clave, foto_perfil, rol_id) VALUES (%s, %s, %s, %s, %s)"
    datos_usuario = (nombre, correo, clave, foto_perfil, rol_id)
    cursor.execute(insert_query, datos_usuario)
    database.commit()
    cursor.close()
#---------Inicio de sesion
def iniciar_sesion(correo, clave):
    cursor = database.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE correo = %s AND clave = %s"
    cursor.execute(query, (correo, clave))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

#FUNCIONES DE GESTION DE PERFIL

def obtener_usuario_por_id(usuario_id):
    cursor = database.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE usuario_id = %s"
    cursor.execute(query, (usuario_id,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

def editar_perfil(usuario_id, nombre, foto_perfil):
    cursor = database.cursor()
    update_query = "UPDATE usuarios SET nombre = %s, foto_perfil = %s WHERE usuario_id = %s"
    datos_usuario = (nombre, foto_perfil, usuario_id)
    cursor.execute(update_query, datos_usuario)
    database.commit()
    cursor.close()

# FUNCIONES PARA EVENTOS

#------------Crear eventos

def crear_evento(titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id):
    cursor = database.cursor()
    insert_query = "INSERT INTO evento (titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    datos_evento = (titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id)
    cursor.execute(insert_query, datos_evento)
    database.commit()
    cursor.close()

def obtener_evento_por_id(evento_id):
    cursor = database.cursor(dictionary=True)
    query = "SELECT * FROM evento WHERE evento_id = %s"
    cursor.execute(query, (evento_id,))
    evento = cursor.fetchone()
    cursor.close()
    return evento

def obtener_eventos():
    cursor = database.cursor(dictionary=True)
    query = "SELECT * FROM evento"
    cursor.execute(query)
    eventos = cursor.fetchall()
    cursor.close()
    return eventos

#Lista a eventos y registro a eventos
def registrar_en_evento(usuario_id, evento_id):
    cursor = database.cursor()
    insert_query = "INSERT INTO registros_eventos (usuario_id, evento_id) VALUES (%s, %s)"
    datos_registro = (usuario_id, evento_id)
    cursor.execute(insert_query, datos_registro)
    database.commit()
    cursor.close()

def obtener_registros_de_evento(evento_id):
    cursor = database.cursor(dictionary=True)
    query = "SELECT usuarios.* FROM registros_eventos INNER JOIN usuarios ON registros_eventos.usuario_id = usuarios.usuario_id WHERE registros_eventos.evento_id = %s"
    cursor.execute(query, (evento_id,))
    registros = cursor.fetchall()
    cursor.close()
    return registros
#NOTIFICACIONES
def enviar_notificacion(usuario_id, evento_id, mensaje):
    cursor = database.cursor()
    insert_query = "INSERT INTO notificaciones (usuario_id, evento_id, mensaje) VALUES (%s, %s, %s)"
    datos_notificacion = (usuario_id, evento_id, mensaje)
    cursor.execute(insert_query, datos_notificacion)
    database.commit()
    cursor.close()

def obtener_notificaciones_usuario(usuario_id):
    cursor = database.cursor(dictionary=True)
    query = "SELECT * FROM notificaciones WHERE usuario_id = %s"
    cursor.execute(query, (usuario_id,))
    notificaciones = cursor.fetchall()
    cursor.close()
    return notificaciones
