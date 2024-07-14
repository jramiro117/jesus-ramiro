import mysql.connector

# Conexión a la base de datos MySQL
database = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',  # Coloca tu contraseña de MySQL aquí
    database='eventos'
)

# Función para registrar un nuevo usuario
def registrar_usuario(nombre, correo, clave, foto_perfil, rol_id):
    try:
        cursor = database.cursor()
        insert_query = "INSERT INTO usuarios (nombre, correo, clave, foto_perfil, rol_id) VALUES (%s, %s, %s, %s, %s)"
        datos_usuario = (nombre, correo, clave, foto_perfil, rol_id)
        cursor.execute(insert_query, datos_usuario)
        database.commit()
        cursor.close()
        print(f"Usuario registrado exitosamente: {nombre}, {correo}, {rol_id}")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
        database.rollback()

# Función para iniciar sesión de usuario
def iniciar_sesion(correo, clave):
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE correo = %s AND clave = %s"
        cursor.execute(query, (correo, clave))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    except mysql.connector.Error as error:
        print(f"Error al iniciar sesión: {error}")
        return None

# Función para obtener un usuario por su ID
def obtener_usuario_por_id(usuario_id):
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE usuario_id = %s"
        cursor.execute(query, (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    except mysql.connector.Error as error:
        print(f"Error al obtener usuario por ID: {error}")
        return None

# Función para editar el perfil de un usuario
def editar_perfil(usuario_id, nombre, foto_perfil):
    try:
        cursor = database.cursor()
        update_query = "UPDATE usuarios SET nombre = %s, foto_perfil = %s WHERE usuario_id = %s"
        datos_usuario = (nombre, foto_perfil, usuario_id)
        cursor.execute(update_query, datos_usuario)
        database.commit()
        cursor.close()
        print(f"Perfil de usuario actualizado: {usuario_id}")
    except mysql.connector.Error as error:
        print(f"Error al editar perfil de usuario: {error}")
        database.rollback()

# Función para crear un nuevo evento
def crear_evento(titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id):
    try:
        cursor = database.cursor()
        insert_query = "INSERT INTO evento (titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        datos_evento = (titulo, descripcion, fecha, hora, lugar, capacidad_maxima, organizador_id)
        cursor.execute(insert_query, datos_evento)
        database.commit()
        cursor.close()
        print(f"Evento creado exitosamente: {titulo}, {fecha}, {organizador_id}")
    except mysql.connector.Error as error:
        print(f"Error al crear evento: {error}")
        database.rollback()

# Función para obtener un evento por su ID
def obtener_evento_por_id(evento_id):
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT * FROM evento WHERE evento_id = %s"
        cursor.execute(query, (evento_id,))
        evento = cursor.fetchone()
        cursor.close()
        return evento
    except mysql.connector.Error as error:
        print(f"Error al obtener evento por ID: {error}")
        return None

# Función para obtener todos los eventos
def obtener_eventos():
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT * FROM evento"
        cursor.execute(query)
        eventos = cursor.fetchall()
        cursor.close()
        return eventos
    except mysql.connector.Error as error:
        print(f"Error al obtener eventos: {error}")
        return None

# Función para registrar a un usuario en un evento
def registrar_en_evento(usuario_id, evento_id):
    try:
        cursor = database.cursor()
        insert_query = "INSERT INTO registros_eventos (usuario_id, evento_id) VALUES (%s, %s)"
        datos_registro = (usuario_id, evento_id)
        cursor.execute(insert_query, datos_registro)
        database.commit()
        cursor.close()
        print(f"Usuario registrado en evento: {usuario_id}, {evento_id}")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario en evento: {error}")
        database.rollback()

# Función para obtener registros de usuarios en un evento
def obtener_registros_de_evento(evento_id):
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT usuarios.* FROM registros_eventos INNER JOIN usuarios ON registros_eventos.usuario_id = usuarios.usuario_id WHERE registros_eventos.evento_id = %s"
        cursor.execute(query, (evento_id,))
        registros = cursor.fetchall()
        cursor.close()
        return registros
    except mysql.connector.Error as error:
        print(f"Error al obtener registros de evento: {error}")
        return None

# Función para enviar una notificación a un usuario
def enviar_notificacion(usuario_id, evento_id, mensaje):
    try:
        cursor = database.cursor()
        insert_query = "INSERT INTO notificaciones (usuario_id, evento_id, mensaje) VALUES (%s, %s, %s)"
        datos_notificacion = (usuario_id, evento_id, mensaje)
        cursor.execute(insert_query, datos_notificacion)
        database.commit()
        cursor.close()
        print(f"Notificación enviada a usuario: {usuario_id}, {evento_id}")
    except mysql.connector.Error as error:
        print(f"Error al enviar notificación: {error}")
        database.rollback()

# Función para obtener notificaciones de un usuario
def obtener_notificaciones_usuario(usuario_id):
    try:
        cursor = database.cursor(dictionary=True)
        query = "SELECT * FROM notificaciones WHERE usuario_id = %s"
        cursor.execute(query, (usuario_id,))
        notificaciones = cursor.fetchall()
        cursor.close()
        return notificaciones
    except mysql.connector.Error as error:
        print(f"Error al obtener notificaciones de usuario: {error}")
        return None

# Función de prueba para agregar un usuario inicial
def agregar_usuario_prueba():
    try:
        cursor = database.cursor()
        insert_query = "INSERT INTO usuarios (nombre, correo, clave, rol_id) VALUES (%s, %s, %s, %s)"
        datos_usuario = ('Usuario Prueba', 'prueba@example.com', 'clave123', 1)  # Ejemplo de datos de prueba
        cursor.execute(insert_query, datos_usuario)
        database.commit()
        cursor.close()
        print("Usuario de prueba agregado exitosamente.")
    except mysql.connector.Error as error:
        print(f"Error al agregar usuario de prueba: {error}")
        database.rollback()

# Llamamos a la función para agregar el usuario de prueba si ejecutamos db.py directamente
if __name__ == '__main__':
    agregar_usuario_prueba()
