from flask import current_app as app
from flask import render_template

#Se pueden declarar una o mas rutas para la funcion que responde a dicha ruta

@app.route('/')
@app.route('/inicio')
def home():
    #Aqui se hace procesamiento y se devuelve una template renderizada, tambien se pueden agregar variables
    return render_template('index.html', title='Inicio')