import sqlite3
from flask import g
from flask import current_app as app

def get_conexion() -> sqlite3.Connection:
    if 'db' not in g:
        db: sqlite3.Connection = sqlite3.connect(app.config['RUTA_DB'])
        g.db = db
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def cerrar_conexion(e: Exception = None):
    db = g.pop('db', None)
    if db is not None:
        db.close()