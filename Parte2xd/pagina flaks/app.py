import mysql.connector
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port='3305',  # Puerto de la base de datos
        user='root',  # Cambia esto por tu usuario
        password='',  # Cambia esto por tu contraseña
        database='datos'  # Asegúrate de que la base de datos 'datos' exista
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registros')
    registros = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', registros=registros)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        edad = request.form['edad']
        email = request.form['email']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO registros (nombre, apellido_paterno, apellido_materno, edad, email) VALUES (%s, %s, %s, %s, %s)',
            (nombre, apellido_paterno, apellido_materno, edad, email)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM registros WHERE id = %s', (id,))
    registro = cursor.fetchone()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        edad = request.form['edad']
        email = request.form['email']
        
        cursor.execute(
            'UPDATE registros SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, edad = %s, email = %s WHERE id = %s',
            (nombre, apellido_paterno, apellido_materno, edad, email, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.close()
    conn.close()
    return render_template('update.html', registro=registro)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM registros WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
