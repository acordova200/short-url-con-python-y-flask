from flask import Flask, render_template, url_for, flash, request, redirect
from flask_mysql_connector import MySQL
import shortuuid

# inicializamos app
app = Flask(__name__)

# endpoint
endpoint = 'http://short.url'

# Conexión MySql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE'] = 'db_enlaces_cortos'

# iniciamos la Base de Datos
mysql = MySQL(app)


# llave secreta para user mensajes flash
app.secret_key = "C1v3S3cr3t4"


# Ruta Inicial
@app.route('/', methods=['GET'])
def inicio():
    try:
        return render_template('index.html'), 200
    except:
        return render_template('404.html'), 404


# Ruta para Crear Enlace Corto y Almacenar en la Base de Datos
@app.route('/crear_enlace_corto', methods=['POST'])
def crear_enlace_corto():
    try:
        if request.method == 'POST':
            # Capturamos la url
            url = request.form['url']
            cursor = mysql.connection.cursor()

            # Ciclo para validar enlace corto que no se duplique
            while True:
                # Generamos el enlace corto
                enlace_corto = shortuuid.ShortUUID().random(length=7)
                # Consultamos a la Base de Datos si existe enlace corto
                cursor.execute(
                    "SELECT * FROM ENLACES WHERE ENLACE_CORTO = BINARY %s", (enlace_corto,))

                if not cursor.fetchone():
                    break

            # Consultamos si en la base de datos existe URL
            cursor.execute(
                "SELECT ENLACE_CORTO FROM ENLACES WHERE URL = BINARY %s", (url,))
            data = cursor.fetchone()
            if data:
                flash(endpoint + '/'+data[0])
                return redirect(url_for('inicio')), 302

            # Ingresamos en la base de datos la url enviada
            cursor.execute(
                "INSERT INTO enlaces (url, enlace_corto) VALUES (%s,%s)", (url, enlace_corto))

            # Guardamos cambios en Base de Datos
            mysql.connection.commit()

            # Cerramos la conexión de la base de datos
            cursor.close()
            nuevo_enlace = endpoint + '/'+enlace_corto
            flash(nuevo_enlace)
            return redirect(url_for('inicio')), 302
    except:
        return render_template('404.html'), 404


# Ruta para ir a URL de Base de Datos
@app.route('/<id>')
def obtener_url(id):
    try:
        cursor = mysql.connection.cursor()

        # Buscamos en la base de datos la dirección URL
        cursor.execute(
            "SELECT URL FROM ENLACES WHERE ENLACE_CORTO = BINARY %s", (id,))

        # Guardamos en variable el resultado
        data = cursor.fetchone()

        # Cerrar Conexión de la Base de Datos
        cursor.close()
        return render_template('ads.html', url=data[0]), 200
    except:
        return render_template('404.html'), 404


# corremos app
if __name__ == "__main__":
    app.run(port=80, debug=True)
