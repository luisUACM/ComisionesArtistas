from ..modelo.model import *

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
    retrato4 = Arte(valkalyh,'arte_portafolio/7.jpg','Micha_Maestra',7,['Retrato', 'Busto', 'Fondo simple'],'Felicitación Maestra Micha')
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

    sol_retrato = SolicitudComision(s_retrato, date.today, '', 1, True)

    valkalyh.servicios = [s_retrato, s_oc, s_logo]
    akali.servicios = [s_juego, s_overlay, s_pixel]
    wichigod.servicios = [s_foto]
    usuarios: list[Usuario] = [valkalyh, akali, wichigod, pepe, luis, edwar]
    
    chat_inicial = Chat(valkalyh, pepe, 1, esta_deacuerdo=(False, True))
    chat_aprobado = Chat(valkalyh, pepe, 2, esta_deacuerdo=(True, True))
    chat_pagado = Chat(valkalyh, pepe, 3, esta_deacuerdo=(True, True))
    chat_extra = Chat(valkalyh, pepe, 4, esta_deacuerdo=(True, True), solicitud_cambios=True)
    chat_pagado2 = Chat(valkalyh, pepe, 5, esta_deacuerdo=(True, True))
    chat_completo = Chat(valkalyh, pepe, 6, esta_deacuerdo=(True, True))
    chat_archivado = Chat(valkalyh, pepe, 7, esta_deacuerdo=(True, True))

    com_inicial = Comision(chat_inicial, sol_retrato, 1,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.SOLICITADA)
    com_aprobado = Comision(chat_aprobado, sol_retrato, 2,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.POR_PAGAR)
    com_pagado = Comision(chat_pagado, sol_retrato, 3,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.EN_PROCESO)
    com_extra = Comision(chat_extra, sol_retrato, 4,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.EN_PROCESO)
    com_pagado2 = Comision(chat_pagado2, sol_retrato, 3,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.EN_PROCESO)
    com_completo = Comision(chat_completo, sol_retrato, 5,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.TERMINADA)
    com_archivado = Comision(chat_archivado, sol_retrato, 6,[c_retrato1, c_retrato3], date.today, estado=Comision.EstadosComision.ARCHIVADA)

    m1 = Mensaje(pepe, 'Hola buenas tardes, me gustaria que me dibujaran un retrato de mi prometida')
    m2 = Mensaje(valkalyh, 'Hola!, si claro, requeriré una imagen de ella como referencia. El costo sería de $450 y la imagen se la entregaría en 1 semana a partir del pago')
    me1 = MensajeEstado(MensajeEstado.EstadoPago.ACTUALIZACION_ACUERDO)
    m3 = Mensaje(pepe, 'Esta bien, en seguida pago')
    m4 = Mensaje(valkalyh, 'Muchas gracias por su preferencia!')
    me2 = MensajeEstado(MensajeEstado.EstadoPago.PAGO_REALIZADO)
    m5 = Mensaje(valkalyh, 'He aquí un boceto general de como se vería. Si me da su visto bueno procederé a terminar el dibujo')
    me3 = MensajeEstado(MensajeEstado.EstadoPago.AVANCE_ENTREGADO)
    m6 = Mensaje(pepe, 'Solo la cabeza? Quiero que se vea de cuerpo completo')
    me4 = MensajeEstado(MensajeEstado.EstadoPago.CAMBIOS_SOLICITADOS)
    m7 = Mensaje(valkalyh, 'Tendría un costo adicional de $400')
    me5 = MensajeEstado(MensajeEstado.EstadoPago.ACTUALIZACION_ACUERDO)
    m8 = Mensaje(pepe, 'Mejor solo de medio cuerpo')
    me6 = MensajeEstado(MensajeEstado.EstadoPago.ACTUALIZACION_ACUERDO)
    me7 = MensajeEstado(MensajeEstado.EstadoPago.CAMBIOS_APROBADOS)
    me8 = MensajeEstado(MensajeEstado.EstadoPago.PAGO_REALIZADO)
    m9 = Mensaje(valkalyh, 'Su dibujo está terminado en seguida lo subo')
    me9 = MensajeEstado(MensajeEstado.EstadoPago.FINALIZADO)
    m10 = Mensaje(valkalyh, 'Un placer hacer negocios :)')
    pago_1 = Pago(com_pagado, pepe, com_pagado.conceptos[0].precio, Pago.EstadoPago.PAGADO)
    pago_2 = Pago(com_completo, pepe, com_completo.conceptos[1].precio, Pago.EstadoPago.PAGADO)
    
    chat_inicial.comision = com_inicial
    chat_aprobado.comision = com_aprobado
    chat_pagado.comision = com_pagado
    chat_extra.comision = com_extra
    chat_pagado2.comision = com_pagado2
    chat_completo.comision = com_completo
    chat_archivado.comision = com_archivado

    chat_inicial.mensajes = [m1, m2]
    chat_aprobado.mensajes = [m1, m2, m3, m4]
    chat_pagado.mensajes = [m1, m2, m3, m4, m5]
    chat_extra.mensajes = [m1, m2, m3, m4, m5, m6, m7, m8]
    chat_pagado2.mensajes = [m1, m2, m3, m4, m5, m6, m7, m8]
    chat_completo.mensajes = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
    chat_archivado.mensajes = [m1, m2, me1, m3, m4, me2, m5, me3, m6 ,me4, m7 ,me5, m8 ,me6, me7, me8, m9, me9, m10]
    com_pagado.pagos = [pago_1]
    com_extra.pagos = [pago_1]
    com_pagado2.pagos = [pago_1, pago_2]
    com_completo.pagos = [pago_1, pago_2]
    com_archivado.pagos = [pago_1, pago_2]

    chats = [chat_inicial, chat_aprobado, chat_pagado, chat_extra, chat_pagado2, chat_completo, chat_archivado]
    comisiones = [com_inicial, com_aprobado, com_pagado, com_extra, com_pagado2, com_completo, com_archivado]
    valkalyh.comisiones = comisiones
    pepe.comisiones = comisiones

    def get_usuario(self, id: int) -> Usuario:
        return self.usuarios[id - 1]
    
    def get_artistas(self) -> list[Usuario]:
        return [self.valkalyh, self.akali, self.wichigod]
    
    def get_etiquetas(self) -> list[str]:
        lista: list[str] = []
        for u in self.usuarios:
            if u.es_artista():
                for a in u.portafolio:
                    for e in a.etiquetas:
                        if e not in lista:
                            lista.append(e)
        return lista
    
    def get_servicios(self) -> list[Servicio]:
        lista = []
        for u in self.usuarios:
            if u.es_artista():
                for s in u.servicios:
                    if s not in lista:
                        lista.append(s)
        return lista