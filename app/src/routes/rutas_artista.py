from flask import current_app as app
from flask import render_template
from flask import send_from_directory
from ..persistence.dao.usuarioDao import UsuarioDao
from ..modelo.model import Usuario
from ..modelo.model import Arte
from ..modelo.model import ServicioComision
from ..modelo.model import Dinero

dao_usuario: UsuarioDao = UsuarioDao()

#NOTA: requiere id de artista en URL para ingresar a su perfil

@app.route('/artista/<int:id>')
def perfil_artista(id: int):
    artista = Usuario('test@gmail', '123', 'Misaki', Usuario.Rol.ARTISTA, 1, 
                    biografia='🇲🇽| Noob | Lic. en Diseño Gráfico 🖋| Clip Studio Paint | No le hago nariz a los Chibis | 3/3 | ☕️',
                    redes_sociales=[(Usuario.RedSocial.OTRA, 'https://vgen.co/misakibyakko'), 
                                    (Usuario.RedSocial.TWITTER, 'https://x.com/MisakiByakko')],
                    foto_perfil='fotos_perfil/1.jpg' )
    portafolio: list[Arte] = [
                            Arte(artista, 'arte_portafolio/1.png', '1', 'png'),
                            Arte(artista, 'arte_portafolio/2.png', '2', 'png'),
                            Arte(artista, 'arte_portafolio/3.png', '3', 'png'),
                            Arte(artista, 'arte_portafolio/4.png', '4', 'png')
                            ]
    servicio = ServicioComision('Chibis originales', 
                            ('Dibujo de personaje original en estilo chibi animado. A cuerpo completo y color', Dinero(100), True), 
                            [Arte(artista, 'arte_portafolio/1.png', '1', 'png'), Arte(artista, 'arte_portafolio/2.png', '2', 'png')], 
                            'Contrato.txt')
    artista.portafolio = portafolio
    artista.comisiones = [servicio, servicio]
    return render_template(
        'perfil_artista.html', 
        title=artista.nombre, 
        artista=artista,
        archivo='fotos_perfil/1.webp'
        )

@app.route('/uploads/<path:archivo>')
def uploads(archivo: str):
    return send_from_directory('uploads', archivo)