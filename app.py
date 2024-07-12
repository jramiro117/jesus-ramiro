# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)  # Configura CORS para permitir peticiones de otros dominios

# Ruta para renderizar registro.html y manejar el registro de usuario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener datos del formulario de registro
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        foto_perfil = request.form.get('fotoPerfil', None)  # Puede ser opcional
        rol_id = int(request.form['rolId'])  # Asegúrate de convertir a entero si es necesario

        # Llama a la función de registro de usuario en db.py
        db.registrar_usuario(nombre, correo, clave, foto_perfil, rol_id)

        return jsonify({'mensaje': 'Usuario registrado exitosamente'})

    # Si es GET, simplemente renderiza el formulario de registro
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
