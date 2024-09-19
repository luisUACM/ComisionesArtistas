from flask import current_app as app
from flask import render_template
from ..persistence.dao.UsuarioDao import UsuarioDao
from ..modelo.usuario import Usuario

usuario_dao = UsuarioDao()

#Se pueden declarar una o mas rutas para la funcion que responde a dicha ruta

@app.route('/')
@app.route('/inicio')
def home():
    #Aqui se hace procesamiento y se devuelve una template renderizada, tambien se pueden agregar variables

    
    usuario_dao.guardar(Usuario(correo='luis@gmail.com', contrasena='123'))
    return render_template('index.html', title='Inicio')