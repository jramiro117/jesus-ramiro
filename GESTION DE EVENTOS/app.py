from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import db

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave segura en producción

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        # Obtener datos del formulario de registro
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        rol_id = int(request.form['rolId'])

        # Llama a la función de registro de usuario en db.py
        db.registrar_usuario(nombre, correo, clave, None, rol_id)  # Cambia foto_perfil a None

        return jsonify({'mensaje': 'Usuario registrado exitosamente'})

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']

        # Verificar credenciales usando la función de inicio de sesión en db.py
        usuario = db.iniciar_sesion(correo, clave)

        if usuario:
            # Guardar el usuario en la sesión
            session['usuario_id'] = usuario['usuario_id']
            session['nombre'] = usuario['nombre']
            session['rol_id'] = usuario['rol_id']

            return jsonify({'mensaje': 'Inicio de sesión exitoso'})
        else:
            return jsonify({'error': 'Credenciales incorrectas'}), 401

if __name__ == '__main__':
    app.run(debug=True)
