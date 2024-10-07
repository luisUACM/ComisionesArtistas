from flask import current_app as app
from flask import render_template
from flask import g
from ..persistence.dao.usuario_dao import UsuarioDao
from ..modelo.model import Usuario
from ..modelo.model import Arte
from ..modelo.model import Servicio
from ..modelo.model import Dinero
from ..modelo.model import Contacto
from ..modelo.model import Concepto
from ..modelo.model import Chat
from ..modelo.model import Comision
from ..modelo.model import Mensaje
from ..modelo.model import Pago
from datetime import date
from ..modelo.fabrica_objetos import FabricaObjetos

dao_usuario: UsuarioDao = UsuarioDao()
fabrica: FabricaObjetos = FabricaObjetos()

@app.route('/artista/<int:id>')
def artista(id: int):
    usuario = fabrica.get_usuario(id)

    es_artista = False
    es_cliente = False
    for r in usuario.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=usuario.nombre, 
        usuario=usuario,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/mi_perfil')
def perfil():
    id = g.id_cuenta
    usuario = fabrica.get_usuario(id)
    es_artista = False
    es_cliente = False
    for r in usuario.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=usuario.nombre, 
        usuario=usuario,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/chat/<int:id>')
def chat(id: int):
    ch = fabrica.ch
    return render_template('chat.html', chat=ch)