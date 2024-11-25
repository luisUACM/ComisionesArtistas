from flask import current_app as app
from flask import render_template
from flask import g
from ..persistence.dao.usuario_dao import UsuarioDao
from ..modelo.model import Usuario, Servicio
from ..modelo.fabrica_objetos import FabricaObjetos
from ..modelo.api_firmas import mandar_correo

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
        es_cliente = es_cliente,
        titulo='Perfil de '+usuario.nombre
        )

@app.route('/mi_perfil')
def perfil():
    id = g.id_cuenta
    usuario = fabrica.get_usuario(id)
    es_artista = usuario.es_artista()
    es_cliente = usuario.es_cliente()

    return render_template(
        'perfil_artista.html', 
        title=usuario.nombre, 
        usuario=usuario,
        es_artista = es_artista,
        es_cliente = es_cliente,
        titulo='Mi perfil'
        )

@app.route('/chat/<int:id>')
def chat(id: int):
    chat = fabrica.chats[id - 1]
    if g.id_cuenta == chat.artista.id:
        titulo = 'Chat de ' + chat.cliente.nombre
    else:
        titulo = 'Chat de ' + chat.artista.nombre
    return render_template('chat.html', chat=chat, titulo=titulo)

@app.route('/comisionar/<int:id>')
def comisionar(id: int):
    servicio: Servicio = fabrica.get_servicio(id)
    titulo = servicio.titulo
    return render_template('comisionar.html', titulo=titulo, servicio=servicio)

@app.route('/firmar/<int:id>')
def firmar(id: int):
    comision = fabrica.get_comision(id)
    return render_template('firmar.html', titulo='Paga tu servicio', comision=comision)

@app.route('/postfirmar/<int:id>')
def postfirmar(id: int):
    comision = fabrica.get_comision(id)
    print('Id contrato:',comision.contrato.id)
    print('Correo:',comision.chat.cliente.correo)
    mandar_correo(comision.contrato.id, comision.chat.cliente)
    return render_template('postfirmar.html')