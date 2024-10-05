from flask import current_app as app
from flask import render_template
from flask import g
from ..persistence.dao.usuarioDao import UsuarioDao
from ..modelo.model import Usuario
from ..modelo.model import Arte
from ..modelo.model import Servicio
from ..modelo.model import Dinero
from ..modelo.model import Contacto
from ..modelo.model import Concepto
from ..modelo.model import Chat

dao_usuario: UsuarioDao = UsuarioDao()
a = Usuario('test@gmail', '123', 'Misaki', [Usuario.Rol.ARTISTA], 1, 
                    biografia='🇲🇽| Noob | Lic. en Diseño Gráfico 🖋| Clip Studio Paint | No le hago nariz a los Chibis | 3/3 | ☕️',
                    contactos=[(Contacto.TipoContacto.OTRA, 'https://vgen.co/misakibyakko'), 
                                    (Contacto.TipoContacto.TWITTER, 'https://x.com/MisakiByakko')],
                    foto_perfil='fotos_perfil/1.jpg' )
a2 = Usuario('test2@gmail', '123', 'Pepe', [Usuario.Rol.CLIENTE], 2, 
                    biografia='',
                    contactos=[])
p: list[Arte] = [
                        Arte(a, 'arte_portafolio/1.png', '1', 'png'),
                        Arte(a, 'arte_portafolio/2.png', '2', 'png'),
                        Arte(a, 'arte_portafolio/3.png', '3', 'png'),
                        Arte(a, 'arte_portafolio/4.png', '4', 'png')
                        ]
co = Concepto('fsgsfdg', Dinero(100), False)
s = Servicio('Chibis originales', 
                        ('Dibujo de personaje original en estilo chibi animado. A cuerpo completo y color', Dinero(100), True), 
                        [Arte(a, 'arte_portafolio/1.png', '1', 'png'), Arte(a, 'arte_portafolio/2.png', '2', 'png')], 
                        'Contrato.txt')
ch = Chat(a, a2)
s.conceptos = [co]
a.portafolio = p
a.servicios = [s, s, s]

#NOTA: requiere id de artista en URL para ingresar a su perfil
@app.route('/artista/<int:id>')
def artista(id: int):
    a.id = id
    es_artista = False
    es_cliente = False
    for r in a.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=a.nombre, 
        usuario=a,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/mi_perfil')
def perfil():
    id = g.id_cuenta
    
    es_artista = False
    es_cliente = False
    for r in a.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=a.nombre, 
        usuario=a,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/chat/<int:id>')
def chat(id: int):
    ch.id=id
    return render_template('chat.html', chat=ch)