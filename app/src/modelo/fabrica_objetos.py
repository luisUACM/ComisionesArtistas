from ..modelo.model import *

"""
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
"""

class FabricaObjetos:
    CONTRATO_GENERICO = """
<div class="text-center h2"><strong>Contrato de prestación de servicios</strong></div><br><br>
El Artista acuerda prestar sus servicios de creación de arte digital al Cliente conforme a las siguientes cláusulas:
<br>
1.- <strong>Propiedad del Arte</strong><br>El artista conserva todos los derechos de autor y propiedad intelectual sobre la obra de arte comisionada.

2.- <strong>Licencia de Uso Personal</strong><br>El cliente recibe una licencia no exclusiva, no transferible y de uso personal para la obra de arte. El cliente puede usar la obra de arte comisionada únicamente para fines personales (como fondos de pantalla, impresiones para uso personal, etc.).

3.- <strong>Uso Comercial</strong><br>El cliente no tiene derecho a usar la obra de arte para ningún propósito comercial, incluyendo pero no limitado a, la venta, distribución, o reproducción con fines de lucro, sin el previo consentimiento por escrito del artista.

4.- <strong>Pago</strong><br>El cliente acuerda pagar conforme a los servicios solicitados indicados en la plataforma al artista por la creación de la obra de arte, el cual deberá ser abonado al inicio de la comisión.

5.- <strong>Entrega</strong><br>El artista entregará la obra de arte digital al cliente dentro del plazo de días acordado por ambas partes a partir de la recepción del pago completo.
"""

    valkalyh = Usuario('valkalyh@gmail.com', '123', 'Valkalyh', [Usuario.Rol.ARTISTA], 1, 
            biografia='26 | ᴀʀᴛ & ᴅᴇsɪɢɴ | ɢᴀᴍɪɴɢ | ɪɴғᴘ | ᴋ-ᴘᴏᴘ | sᴘᴀɴɪsʜ & ᴇɴɢʟɪsʜ | ♡ |',
            contactos=[(Contacto.TipoContacto.INSTAGRAM, 'https://www.instagram.com/valkalyh_/'), 
                    (Contacto.TipoContacto.CORREO, 'valkalyhofficial@gmail.com')],
            foto_perfil='fotos_perfil/1.png')

    akali = Usuario('akali@gmail.com', '123', 'Akali', [Usuario.Rol.ARTISTA], 2, 
            biografia='🎨 Artista de Pixel Art | 🎮 Diseño de videojuegos y overlays personalizados para streamers | Transforma tu mundo digital en 8 bits ✨ ¡Comisiones abiertas! 🚀',
            contactos=[(Contacto.TipoContacto.TWITCH, 'https://www.twitch.tv/akali'), 
                    (Contacto.TipoContacto.TWITTER, 'https://x.com/akali')],
            foto_perfil='fotos_perfil/2.jpg')

    wichigod = Usuario('wichigod@gmail.com', '123', 'WICHIGOD', [Usuario.Rol.ARTISTA], 3, 
            biografia='📸 Fotógrafo Profesional | Capturando momentos únicos y emociones auténticas 🌟 Especializado en fotografía de paisaje | ¡Tu historia merece ser contada! 🌍',
            contactos=[(Contacto.TipoContacto.INSTAGRAM, 'https://www.instagram.com/WICHIGOD/'), 
                    (Contacto.TipoContacto.KOFI, 'https://ko-fi.com/WICHIGOD')],
            foto_perfil='fotos_perfil/3.jpg')
    pepe = Usuario('pepe@gmail', '123', 'Pepe', [Usuario.Rol.CLIENTE], 4)
    luis = Usuario('luis@gmail', '123', 'Luis', [Usuario.Rol.CLIENTE], 5)
    edwar = Usuario('edwar@gmail', '123', 'Edwar', [Usuario.Rol.CLIENTE], 6)

    retrato1 = Arte(valkalyh,'arte_portafolio/1.jpg','Cry_Black_Angel',1,['Medio cuerpo', 'Retrato'],'Fanart Cry Black Angel')
    retrato2 = Arte(valkalyh,'arte_portafolio/2.jpg','Cry_Fanart',2,['Busto', 'Retrato'],'Cry Fanart')
    juego1 = Arte(akali,'arte_portafolio/3.jpg','D.va',3,['Medio cuerpo', 'Videojuegos', 'Fanart', 'Overwatch'],'D.va Overwatch')
    oc1 = Arte(valkalyh,'arte_portafolio/4.jpg','Dragon_Fruit_Girl',4,['Busto', 'Original Character'],'Dragon Fruit Girl')
    retrato3 = Arte(valkalyh,'arte_portafolio/5.jpg','Velour_2023',5,['Foto de perfil', 'Retrato'],'Velour 2023')
    oc2 = Arte(valkalyh,'arte_portafolio/6.jpg','Muerte_Re_Draw',6,['Medio cuerpo', 'Original Character'],'Muerte Re-Draw')
    retrato4 = Arte(valkalyh,'arte_portafolio/7.jpg','Micha_Maestra',7,['Retrato', 'Busto', 'Fondo Simple'],'Felicitación Maestra Micha')
    overlay1 = Arte(akali,'arte_portafolio/8.jpg','Stream_Overlay_Gancyto_Mesa_de_trabajo_1',8,['Stream overlay', 'Emote'],'Stream Overlay Gancyto')
    pixel1 = Arte(akali,'arte_portafolio/9.jpg','Clove_Pixel',9,['Pixelart', 'Videojuegos', 'Fanart','Valorant'],'Clove Pixelart')
    pixel2 = Arte(akali,'arte_portafolio/10.jpg','Sage_Pixel',10,['Pixelart', 'Videojuegos', 'Fanart','Valorant'],'Sage Pixelart')
    pixel3 = Arte(akali,'arte_portafolio/11.jpg','Chamber_Pixel',11,['Pixelart', 'Videojuegos', 'Fanart','Valorant'],'Chamber Pixelart')
    logo1 = Arte(valkalyh,'arte_portafolio/12.png','image',12,['Logotipo'],'Network.MX logo')
    logo2 = Arte(valkalyh,'arte_portafolio/13.jpg','photo_2024-10-04_14-27-56',13,['Logotipo'],'Happy Place logo')
    juego2 = Arte(akali,'arte_portafolio/14.jpg','Pink_Mercy_1',14,['Medio cuerpo', 'Videojuegos', 'Fanart', 'Overwatch'],'Pink Mercy')
    juego3 = Arte(akali,'arte_portafolio/15.jpg','Dan_March',15,['Medio cuerpo', 'Videojuegos', 'Fanart', 'Honkai Star Rail'],'Dan Heng X March 7th')
    foto1 = Arte(wichigod,'arte_portafolio/16.png','image',16,['Fotografía'],'Puerto Vallarta')
    foto2 = Arte(wichigod,'arte_portafolio/17.png','image',17,['Fotografía'],'Sacramento, Ca')
    foto3 = Arte(wichigod,'arte_portafolio/18.png','image',18,['Fotografía'],'Ansiedad')
    foto4 = Arte(wichigod,'arte_portafolio/19.jpg','3282Foto2',19,['Fotografía'],'Sólida Inversión Propiedades')
    foto5 = Arte(wichigod,'arte_portafolio/20.jpg','42728_1',20,['Fotografía'],'Interior Blanco Minimalista')

    c_retrato1 = Concepto('Retrato de un personaje de tu elección, cuello para arriba', Dinero(450), False)
    c_retrato2 = Concepto('La ilustracion es de busto para arriba', Dinero(100), True)
    c_retrato3 = Concepto('La ilustracion es de cintura para arriba', Dinero(200), True)
    c_retrato4 = Concepto('La ilustracion es de cuerpo completo', Dinero(400), True)
    c_retrato5 = Concepto('Agregar fondo con figuras simples', Dinero(350), True)
    c_juego1 = Concepto('Ilustración de medio cuerpo de personaje de videojuegos', Dinero(800), False)
    c_juego2 = Concepto('Ship con otro personaje', Dinero(400), False)
    c_oc1 = Concepto('Diseño de un personaje original, busto para arriba', Dinero(650), False)
    c_oc2 = Concepto('La ilustracion es de cintura para arriba', Dinero(200), True)
    c_oc3 = Concepto('La ilustracion es de cuerpo completo', Dinero(400), True)
    c_overlay1 = Concepto('Paquete de streamer incluye: \n- 1 overlay (pantalla principal chat y cam)\n- 6 Banners para paneles de información\n- 4 emotes pesonalizados.', Dinero(1170), False)
    c_overlay2 = Concepto('+4 paneles extra', Dinero(200), True)
    c_overlay3 = Concepto('+2 emotes extra', Dinero(320), True)
    c_overlay4 = Concepto('+1 emoticono animado', Dinero(450), True)
    c_pixel1 = Concepto('Pixelart (512 x 512) de personaje de videojuegos con fondo plano', Dinero(280), False)
    c_logo1 = Concepto('Logotipo para empresa. (Incluye derechos de autor)', Dinero(890), False)
    c_logo2 = Concepto('2 Variaciones de color', Dinero(130), True)
    c_foto1 = Concepto('5 Fotografías de paisajes de tu elección con alguna temática en específico. El lugar debe ser dentro del territorio mexicano.', Dinero(10970), False)
    c_foto2 = Concepto('Toma aerea', Dinero(960), True)
    c_foto3 = Concepto('Captura de movimiento', Dinero(1540), True)

    retratos = [retrato1, retrato2, retrato3, retrato4]
    juegos = [juego1, juego2, juego3]
    ocs = [oc1, oc2]
    overlays = [overlay1]
    pixels = [pixel1, pixel2, pixel3]
    logos = [logo1, logo2]
    fotos = [foto1, foto2, foto3, foto4, foto5]

    conceptos_retrato = [c_retrato1, c_retrato2, c_retrato3, c_retrato4, c_retrato5]
    conceptos_juego = [c_juego1, c_juego2]
    conceptos_oc = [c_oc1, c_oc2, c_oc3]
    conceptos_overlay = [c_overlay1, c_overlay2, c_overlay3, c_overlay4]
    conceptos_pixel = [c_pixel1]
    conceptos_logo = [c_logo1, c_logo2]
    conceptos_foto = [c_foto1, c_foto2, c_foto3]

    valkalyh.portafolio = retratos + ocs + logos
    akali.portafolio = juegos + overlays + pixels
    wichigod.portafolio = fotos

    s_retrato = Servicio('Retrato de personaje',conceptos_retrato, retratos, [CONTRATO_GENERICO], 1, valkalyh)
    s_oc = Servicio('Diseño de OC', conceptos_oc, ocs, [CONTRATO_GENERICO], 2, valkalyh)
    s_logo = Servicio('Diseño de logotipo', conceptos_logo, logos, [CONTRATO_GENERICO], 3, valkalyh)
    s_juego = Servicio('Ilustración de personaje de videojuego', conceptos_juego, juegos, [CONTRATO_GENERICO], 4, akali)
    s_overlay = Servicio('Overlay para streamer', conceptos_overlay, overlays, [CONTRATO_GENERICO], 5, akali)
    s_pixel = Servicio('Pixelart de personaje de videojuego', conceptos_pixel, pixels, [CONTRATO_GENERICO], 6, akali)
    s_foto = Servicio('Fotografía de paisaje 4K', conceptos_foto, fotos, [CONTRATO_GENERICO], 7, wichigod)

    valkalyh.servicios = [s_retrato, s_oc, s_logo]
    akali.servicios = [s_juego, s_overlay, s_pixel]
    wichigod.servicios = [s_foto]
    usuarios: list[Usuario] = [valkalyh, akali, wichigod, pepe, luis, edwar]
    
    ch = Chat(valkalyh, pepe, esta_deacuerdo=(True, True), solicitud_cambios=False)
    com = Comision(ch, s_retrato, 1,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.SOLICITADA)

    m1 = Mensaje(pepe, 'Lorem ipsum dolor sit amet consectetur adipiscing elit ultricies hendrerit ante, parturient netus torquent erat egestas vel iaculis porta pharetra convallis, morbi eu metus mi pretium sociis facilisi suspendisse justo. Nibh primis nisi blandit felis pretium leo, proin libero ultrices parturient sapien massa class, et tempor eget diam vestibulum. Imperdiet tempus condimentum dui sodales ultrices proin inceptos, habitant pellentesque justo quis vulputate penatibus turpis sagittis, curabitur vitae quam morbi maecenas vehicula.')
    m2 = Mensaje(valkalyh, 'Lorem ipsum dolor sit amet consectetur adipiscing elit ultricies hendrerit ante, parturient netus torquent erat egestas vel iaculis porta pharetra convallis, morbi eu metus mi pretium sociis facilisi suspendisse justo. Nibh primis nisi blandit felis pretium leo, proin libero ultrices parturient sapien massa class, et tempor eget diam vestibulum. Imperdiet tempus condimentum dui sodales ultrices proin inceptos, habitant pellentesque justo quis vulputate penatibus turpis sagittis, curabitur vitae quam morbi maecenas vehicula.')
    pa1 = Pago(com, pepe, Dinero(100), Pago.EstadoPago.PAGADO)
    ch.comision = com
    ch.mensajes = [m1, m2, m1, m1, m2]
    com.pagos = [pa1]

    def get_usuario(self, id: int) -> Usuario:
        return self.usuarios[id - 1]