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
from ..modelo.model import Comision
from ..modelo.model import Mensaje
from ..modelo.model import Pago
from datetime import date

dao_usuario: UsuarioDao = UsuarioDao()
misaki = Usuario('test@gmail', '123', 'Misaki', [Usuario.Rol.ARTISTA], 1, 
                    biografia='🇲🇽| Noob | Lic. en Diseño Gráfico 🖋| Clip Studio Paint | No le hago nariz a los Chibis | 3/3 | ☕️',
                    contactos=[(Contacto.TipoContacto.OTRA, 'https://vgen.co/misakibyakko'), 
                                    (Contacto.TipoContacto.TWITTER, 'https://x.com/MisakiByakko')],
                    foto_perfil='fotos_perfil/1.jpg' )
pepe = Usuario('test2@gmail', '123', 'Pepe', [Usuario.Rol.CLIENTE], 2, 
                    biografia='',
                    contactos=[])
p: list[Arte] = [
                        Arte(misaki, 'arte_portafolio/1.png', '1', 'png'),
                        Arte(misaki, 'arte_portafolio/2.png', '2', 'png'),
                        Arte(misaki, 'arte_portafolio/3.png', '3', 'png'),
                        Arte(misaki, 'arte_portafolio/4.png', '4', 'png')
                        ]
co = Concepto('Lorem ipsum dolor sit amet consectetur adipiscing elit class aliquet porta, nostra aliquam nisl fringilla', Dinero(100), False)
co2 = Concepto('Lorem ipsum dolor sit amet consectetur adipiscing elit class aliquet porta, nostra aliquam nisl fringilla', Dinero(150), True)
s = Servicio('Chibis originales', 
                        ('Dibujo de personaje original en estilo chibi animado. A cuerpo completo y color', Dinero(100), True), 
                        [Arte(misaki, 'arte_portafolio/1.png', '1', 'png'), Arte(misaki, 'arte_portafolio/2.png', '2', 'png')], 
                        'Contrato.txt')
ch = Chat(misaki, pepe, esta_deacuerdo=(True, True), solicitud_cambios=False)
com = Comision(ch, s, 1, [co, co], date.today, estado=Comision.EstadosComision.SOLICITADA)

m1 = Mensaje(pepe, 'Lorem ipsum dolor sit amet consectetur adipiscing elit ultricies hendrerit ante, parturient netus torquent erat egestas vel iaculis porta pharetra convallis, morbi eu metus mi pretium sociis facilisi suspendisse justo. Nibh primis nisi blandit felis pretium leo, proin libero ultrices parturient sapien massa class, et tempor eget diam vestibulum. Imperdiet tempus condimentum dui sodales ultrices proin inceptos, habitant pellentesque justo quis vulputate penatibus turpis sagittis, curabitur vitae quam morbi maecenas vehicula.')
m2 = Mensaje(misaki, 'Lorem ipsum dolor sit amet consectetur adipiscing elit ultricies hendrerit ante, parturient netus torquent erat egestas vel iaculis porta pharetra convallis, morbi eu metus mi pretium sociis facilisi suspendisse justo. Nibh primis nisi blandit felis pretium leo, proin libero ultrices parturient sapien massa class, et tempor eget diam vestibulum. Imperdiet tempus condimentum dui sodales ultrices proin inceptos, habitant pellentesque justo quis vulputate penatibus turpis sagittis, curabitur vitae quam morbi maecenas vehicula.')
pa1 = Pago(com, pepe, Dinero(100), Pago.EstadoPago.PAGADO)

s.conceptos = [co, co2]
misaki.portafolio = p
misaki.servicios = [s, s, s]
ch.comision = com
ch.mensajes = [m1, m2, m1, m1, m2]
com.pagos = [pa1]
com.conceptos = [co]
com.pagos = [pa1]

#NOTA: requiere id de artista en URL para ingresar a su perfil
@app.route('/artista/<int:id>')
def artista(id: int):
    misaki.id = id
    es_artista = False
    es_cliente = False
    for r in misaki.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=misaki.nombre, 
        usuario=misaki,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/mi_perfil')
def perfil():
    id = g.id_cuenta
    
    es_artista = False
    es_cliente = False
    for r in misaki.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=misaki.nombre, 
        usuario=misaki,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/chat/<int:id>')
def chat(id: int):
    ch.id=id
    return render_template('chat.html', chat=ch)