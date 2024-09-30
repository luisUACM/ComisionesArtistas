from flask import current_app as app
from flask import render_template
from flask import send_from_directory
from flask import g
from ..persistence.dao.usuarioDao import UsuarioDao
from ..modelo.model import Usuario
from ..modelo.model import Arte
from ..modelo.model import Servicio
from ..modelo.model import Dinero
from ..modelo.model import Contacto

dao_usuario: UsuarioDao = UsuarioDao()

#NOTA: requiere id de artista en URL para ingresar a su perfil

@app.route('/artista/<int:id>')
def artista(id: int):
    artista = Usuario('test@gmail', '123', 'Misaki', [Usuario.Rol.ARTISTA, Usuario.Rol.CLIENTE], id, 
                    biografia='🇲🇽| Noob | Lic. en Diseño Gráfico 🖋| Clip Studio Paint | No le hago nariz a los Chibis | 3/3 | ☕️',
                    contactos=[(Contacto.TipoContacto.OTRA, 'https://vgen.co/misakibyakko'), 
                                    (Contacto.TipoContacto.TWITTER, 'https://x.com/MisakiByakko')],
                    foto_perfil='fotos_perfil/1.jpg' )
    portafolio: list[Arte] = [
                            Arte(artista, 'arte_portafolio/1.png', '1', 'png'),
                            Arte(artista, 'arte_portafolio/2.png', '2', 'png'),
                            Arte(artista, 'arte_portafolio/3.png', '3', 'png'),
                            Arte(artista, 'arte_portafolio/4.png', '4', 'png')
                            ]
    servicio = Servicio('Chibis originales', 
                            ('Dibujo de personaje original en estilo chibi animado. A cuerpo completo y color', Dinero(100), True), 
                            [Arte(artista, 'arte_portafolio/1.png', '1', 'png'), Arte(artista, 'arte_portafolio/2.png', '2', 'png')], 
                            'Contrato.txt')
    artista.portafolio = portafolio
    artista.servicios = [servicio, servicio, servicio]
    
    es_artista = False
    es_cliente = False
    for r in artista.roles:
        if r == Usuario.Rol.ARTISTA:
            es_artista = True
        elif r == Usuario.Rol.CLIENTE:
            es_cliente = True

    return render_template(
        'perfil_artista.html', 
        title=artista.nombre, 
        usuario=artista,
        es_artista = es_artista,
        es_cliente = es_cliente
        )

@app.route('/uploads/<path:filename>')
def uploads(filename: str):
    return send_from_directory('uploads', filename)