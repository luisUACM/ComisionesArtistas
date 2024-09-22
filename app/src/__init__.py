from flask import Flask
import sqlite3

def init_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.secret_key = '123456'
    app.config['UPLOAD_FOLDER'] = 'uploads/'

    app.config['NOMBRE_DB'] = 'database.db'
    app.config['RUTA_DB'] = 'src/persistence/' + app.config['NOMBRE_DB']
    app.config['NOMBRE_SQUEMA'] = 'squema.sql'
    app.config['RUTA_SQUEMA'] = 'src/persistence/' + app.config['NOMBRE_SQUEMA']

    connection = sqlite3.connect(app.config['RUTA_DB'])
    with open(app.config['RUTA_SQUEMA']) as f:
        connection.executescript(f.read())
    connection.close()
    
    with app.app_context():
        #  =========================================================
        #   
        #   Aquí importar todos los archivos que usen el objeto app
        #   
        #  =========================================================

        from .routes import routes
        from .routes import rutas_artista
        from .persistence import db_helper

        return app
    