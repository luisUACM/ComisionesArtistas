from datetime import datetime
from datetime import date
from enum import Enum

#Inicio clase Dinero
class Dinero:

    class TipoMoneda(Enum):

        MXN = 1
        USD = 2

    DICCIONARIO_CONVERSIONES = {'USD-MNX':19.25, 
                                'MNX-USD':0.052}

    def __init__(
                self, 
                cantidad: float,
                moneda: TipoMoneda = TipoMoneda.MXN,
                id: int = None
                ) -> None:
        self._cantidad: float = cantidad
        self._moneda: Dinero.TipoMoneda = moneda
        self._id: int = id

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: float) -> None:
        self._cantidad = cantidad

    @property
    def moneda(self) -> TipoMoneda:
        return self._moneda

    @moneda.setter
    def moneda(self, moneda: TipoMoneda) -> None:
        self._moneda = moneda

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

#Fin clase Dinero

#Inicio clase Usuario
class Usuario:

    class Rol(Enum):

        ARTISTA = 1
        CLIENTE = 2

    def __init__(
                self, 
                correo: str, 
                contrasena: str, 
                nombre: str, 
                roles: list[Rol], 
                id: int = None, 
                biografia: str = '',
                foto_perfil: str = '/fotos_perfil/generic.webp',
                moneda: Dinero.TipoMoneda = Dinero.TipoMoneda.MXN,
                portafolio: list['Arte'] = [],
                comisiones: list['Comision'] = [],
                servicios: list['Servicio'] = [],
                contactos: list['Contacto'] = [],
                saldo: float = 0.0,
                ) -> None:
        
        self._correo: str = correo
        self._contrasena: str = contrasena
        self._nombre: str = nombre
        self._roles: list[Usuario.Rol] = roles
        self._id: int = id
        self._biografia: str = biografia
        self._foto_perfil: str = foto_perfil
        self._moneda: Dinero.TipoMoneda = moneda
        self._portafolio: list[Arte] = portafolio
        self._comisiones: list[Comision] = comisiones
        self._servicios: list[Servicio] = servicios
        self._contactos: list[Contacto] = contactos
        self._saldo: float = saldo

    @property
    def correo(self) -> str:
        return self._correo
    
    @correo.setter
    def correo(self, correo: str):
        self._correo = correo

    @property
    def contrasena(self) -> str:
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, contrasena: str):
        self._contrasena = contrasena
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def roles(self) -> list[Rol]:
        return self._roles
    
    @roles.setter
    def roles(self, roles: list[Rol]):
        self._roles = roles

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def biografia(self) -> str:
        return self._biografia
    
    @biografia.setter
    def biografia(self, biografia: str):
        self._biografia = biografia
    
    @property
    def foto_perfil(self) -> str:
        return self._foto_perfil
    
    @foto_perfil.setter
    def foto_perfil(self, foto_perfil: str):
        self._foto_perfil = foto_perfil
    
    @property
    def moneda(self) -> Dinero.TipoMoneda:
        return self.moneda
    
    @moneda.setter
    def moneda(self, moneda: Dinero.TipoMoneda):
        self.moneda = moneda
    
    @property
    def portafolio(self) -> list['Arte']:
        return self._portafolio
    
    @portafolio.setter
    def portafolio(self, portafolio: list['Arte']):
        self._portafolio = portafolio

    @property
    def comisiones(self) -> list['Comision']:
        return self._comisiones
    
    @comisiones.setter
    def comisiones(self, comisiones: list['Comision']):
        self._comisiones = comisiones

    @property
    def servicios(self) -> list['Servicio']:
        return self._servicios
    
    @servicios.setter
    def servicios(self, servicios: list['Servicio']):
        self._servicios = servicios

    @property
    def contactos(self) -> list['Contacto']:
        return self._contactos
    
    @contactos.setter
    def contactos(self, contactos: list['Contacto']):
        self._contactos = contactos
    
    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self._saldo = saldo 
    
    def esta_disponible(self) -> bool:
        disponible = True
        for c in self.comisiones:
            if c.estado == Comision.EstadosComision.EN_PROCESO or (c.estado == Comision.EstadosComision.POR_PAGAR and len(c.conceptos) > 2):
                disponible = False
        return disponible
    
    def es_artista(self) -> bool:
        es_artista = False
        for r in self.roles:
            if r == Usuario.Rol.ARTISTA:
                es_artista = True
                break
        return es_artista

    def es_cliente(self) -> bool:
        es_cliente = False
        for r in self.roles:
            if r == Usuario.Rol.CLIENTE:
                es_cliente = True
                break
        return es_cliente
#Fin clase usuario

#CLASE Servicio
class Servicio:
    def __init__(
                self, 
                titulo: str, 
                conceptos: list['Concepto'],  
                piezas_arte: list['Arte'],
                contrato: list['Contrato'],
                id: int = None,
                artista: Usuario = None
                ) -> None:
        self._titulo: str = titulo
        self._conceptos: list[Concepto] = conceptos
        self._piezas_arte: list[Arte] = piezas_arte
        self._contrato: Contrato = contrato
        self._id: int = id
        self._artista: Usuario = artista

    def obtener_ruta_primera_arte(self) -> str:
        if self.piezas_arte:
            return self.piezas_arte[0].ruta  # Retorna la ruta de la primera obra de arte
        return ""  # Retorna una cadena vacía si no hay arte en la lista

    def dame_costo_base(self) -> str:
        for concepto in self._conceptos:
            if not concepto.es_extra:  
                costo = concepto.precio._cantidad  
                moneda = concepto.precio.moneda.name  # Asegúrate de que `moneda` sea un enum o un objeto que tenga un atributo `name`.
                return f"${costo:.2f} {moneda}"  # Formato de dos decimales y espacio entre costo y moneda
        return "0.00"  # Si no hay concepto que cumpla la condición, devuelve "0.00"

    def dame_etiquetas(self) -> list[str]:
        # Verificar si hay al menos una pieza de arte en la lista
        if self._piezas_arte:
            # Obtener las etiquetas del primer elemento de la lista de piezas de arte
            return self._piezas_arte[0].etiquetas  # Asumiendo que cada objeto 'Arte' tiene un atributo 'etiquetas'
        return []  # Retornar lista vacía si no hay piezas de arte
    
    def dame_descripcion(self) -> str:
        for concepto in self._conceptos:
            if not concepto.es_extra:  # Verificar si es_extra es False
                return concepto._descripcion # Devuelve la cantidad del precio del concepto
        return 0.0  # Si no hay concepto que cumpla la condición
    
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo

    @property
    def conceptos(self) -> list['Concepto']:
        return self._conceptos

    @conceptos.setter
    def conceptos(self, conceptos: list['Concepto']) -> None:
        self._conceptos = conceptos

    @property
    def piezas_arte(self) -> list['Arte']:
        return self._piezas_arte

    @piezas_arte.setter
    def piezas_arte(self, piezas_arte: list['Arte']) -> None:
        self._piezas_arte = piezas_arte

    @property
    def contrato(self) -> list['Contrato']:
        return self._contrato

    @contrato.setter
    def contrato(self, contrato: list['Contrato']) -> None:
        self._contrato = contrato

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def artista(self) -> Usuario:
        return self._artista

    @artista.setter
    def artista(self, artista: Usuario) -> None:
        self._artista = artista

#Fin clase servicio_comision

class Contrato:
    def __init__(
            self,
            titulo: str,
            contenido: str,
            nombre_artista: str,
            servicio: Servicio,
            id: int = None,
            nombre_cliente: str = None,
            firma = None
            ) -> None:
        self._titulo: str = titulo
        self._contenido: str = contenido
        self._nombre_artista: str = nombre_artista
        self._servicio: Servicio = servicio
        self._id: int = id
        self._nombre_cliente: str = nombre_cliente
        self._firma = firma
        
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo
        
    @property
    def contenido(self) -> str:
        return self._contenido

    @contenido.setter
    def contenido(self, contenido: str) -> None:
        self._contenido = contenido

    @property
    def nombre_artista(self) -> str:
        return self._nombre_artista

    @nombre_artista.setter
    def nombre_artista(self, nombre_artista: str) -> None:
        self._nombre_artista = nombre_artista

    @property
    def servicio(self) -> Servicio:
        return self._servicio

    @servicio.setter
    def servicio(self, servicio: Servicio) -> None:
        self._servicio = servicio
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def nombre_cliente(self) -> str:
        return self._nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente: str) -> None:
        self._nombre_cliente = nombre_cliente

    @property
    def firma(self):
        return self._firma

    @id.setter
    def firma(self, firma) -> None:
        self._firma = firma
#Fin clase Contrato 

#Inicio clase Pago
class Pago:
    
    class EstadoPago(Enum):
        
        EN_PROCESO = 1 #Cuando esperamos la verificacion del pago
        PAGADO = 2 #Cuando ya se verifico al transaccion.
        PENDIENTE = 3 #No se ha pagado por cualquier motivo

    def __init__(
                self,
                comision: 'Comision' = None,   #FK
                cliente: 'Usuario' = None,
                monto: 'Dinero' = None,   
                estado: EstadoPago = EstadoPago.PENDIENTE,
                id: int = None,
                fecha_hora: datetime = datetime.now(),                
                ) -> None:
        self._comision: Comision = comision
        self._cliente: Usuario = cliente
        self._monto: Dinero = monto
        self._estado: Pago.EstadoPago = estado
        self._id: int = id
        self._fecha_hora: datetime = fecha_hora
        
    @property
    def comision(self) -> 'Comision':
        return self._comision

    @comision.setter
    def comision(self, comision: 'Comision') -> None:
        self._comision = comision

    @property
    def cliente(self) -> Usuario:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: Usuario) -> None:
        self._cliente = cliente

    @property
    def monto(self) -> 'Dinero':
        return self._monto

    @monto.setter
    def monto(self, monto: 'Dinero') -> None:
        self._monto = monto

    @property
    def estado(self) -> EstadoPago:
        return self._estado

    @estado.setter
    def estado(self, estado: EstadoPago) -> None:
        self._estado = estado

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora

    @fecha_hora.setter
    def fecha_hora(self, fecha_hora: datetime) -> None:
        self._fecha_hora = fecha_hora
        
#fin clase Pago

#Inicio clase Mensaje
class Mensaje:
    
    def __init__(
                self, 
                usuario: Usuario, 
                mensaje: str, 
                id: int = None, 
                fecha_hora: datetime = datetime.now(), 
                chat: 'Chat' = None,
                ruta_imagen: str = None
                ) -> None:
        self._usuario: Usuario = usuario
        self._mensaje: Mensaje = mensaje
        self._id: int = id
        self._fecha_hora: datetime = fecha_hora
        self._chat: Chat = chat
        self._ruta_imagen: str = ruta_imagen

    @property
    def usuario(self) -> 'Usuario':
        return self._usuario

    @usuario.setter
    def usuario(self, usuario: 'Usuario') -> None:
        self._usuario = usuario

    @property
    def mensaje(self) -> str:
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje: str) -> None:
        self._mensaje = mensaje

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora

    @fecha_hora.setter
    def fecha_hora(self, fecha_hora: datetime) -> None:
        self._fecha_hora = fecha_hora

    @property
    def chat(self) -> 'Chat':
        return self._chat

    @chat.setter
    def chat(self, chat: 'Chat') -> None:
        self._chat = chat

    @property
    def ruta_imagen(self) -> str:
        return self._ruta_imagen

    @ruta_imagen.setter
    def ruta_imagen(self, ruta_imagen: str) -> None:
        self._ruta_imagen = ruta_imagen

#Fin clase mensaje

class MensajeEstado:

    def __init__(
                self, 
                mensaje: str, 
                id: int = None, 
                fecha_hora: datetime = datetime.now(), 
                chat: 'Chat' = None,
                ) -> None:
        self._mensaje: Mensaje = mensaje
        self._id: int = id
        self._fecha_hora: datetime = fecha_hora
        self._chat: Chat = chat

    @property
    def mensaje(self) -> str:
        return self._mensaje

    @mensaje.setter
    def mensaje(self, mensaje: str) -> None:
        self._mensaje = mensaje

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora

    @fecha_hora.setter
    def fecha_hora(self, fecha_hora: datetime) -> None:
        self._fecha_hora = fecha_hora

    @property
    def chat(self) -> 'Chat':
        return self._chat

    @chat.setter
    def chat(self, chat: 'Chat') -> None:
        self._chat = chat

class SolicitudComision:
    
    def __init__(
            self, 
            servicio: Servicio,
            fecha_limite: date,
            detalles: str,
            id: int = None,
            aprobada: bool = False
        ) -> None:
        self._servicio: Servicio = servicio
        self._fecha_limite: date = fecha_limite
        self._detalles: str = detalles
        self._id: int = id
        self._aprobada: bool = aprobada

    @property
    def servicio(self) -> Servicio:
        return self._servicio

    @servicio.setter
    def id(self, servicio: Servicio) -> None:
        self._servicio = servicio
        
    @property
    def fecha_limite(self) -> date:
        return self._fecha_limite
    
    @fecha_limite.setter
    def id(self, fecha_limite: date) -> None:
        self._fecha_limite = fecha_limite

    @property
    def detalles(self) -> str:
        return self._detalles

    @detalles.setter
    def detalles(self, detalles: str) -> None:
        self._detalles = detalles

    @servicio.setter
    def id(self, servicio: Servicio) -> None:
        self._servicio = servicio
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def aprobada(self) -> bool:
        return self._aprobada

    @aprobada.setter
    def aprobada(self, aprobada: bool) -> None:
        self._aprobada = aprobada

#Inicio clase Comision
class Comision:

    class EstadosComision(Enum):
        
        SOLICITADA = 1 #Estado en donde se espera inicar el chat.
        POR_PAGAR = 2 #Estado donde Cliente y Artista estan de acuerdo
        EN_PROCESO = 3 #Paso el pago y se inicia el desarrollo de arte.
        TERMINADA = 4 #El artista sube -> el trabajo de arte fianlizado.
        ARCHIVADA = 5 #El cliente descarga el trabajo realizado <-
        
    def __init__(
                self, 
                chat: 'Chat',
                solicitud_comision: SolicitudComision,
                cantidad: int,
                conceptos: list['Concepto'],
                fecha_entrega: date, 
                id: int = None,
                fecha_solicitud: date = date.today,
                avances: list[str] = [],
                productos_finales: list[str] = [],
                estado: EstadosComision = EstadosComision.SOLICITADA,
                pagos: list[Pago] = None   
                ) -> None:
        self._chat: Chat = chat
        self._solicitud_comision : SolicitudComision = solicitud_comision
        self._cantidad: int = cantidad 
        self._conceptos: list[Concepto] = conceptos
        self._fecha_entrega: date = fecha_entrega
        self._id: int = id
        self._fecha_solicitud: date = fecha_solicitud
        self._avances: list[str] = avances
        self._productos_finales: list[str] = productos_finales
        self._estado = estado
        self._pagos = pagos 

    @property
    def chat(self) -> 'Chat':
        return self._chat

    @chat.setter
    def chat(self, chat: 'Chat') -> None:
        self._chat = chat
    
    @property
    def servicio(self) -> 'Servicio':
        return self._solicitud_comision.servicio

    @servicio.setter
    def servicio(self, servicio: 'Servicio') -> None:
        self._solicitud_comision.servicio = servicio
    
    @property
    def solicitud_comision(self) -> SolicitudComision:
        return self._solicitud_comision

    @solicitud_comision.setter
    def solicitud_comision(self, solicitud_comision: SolicitudComision) -> None:
        self._solicitud_comision = solicitud_comision
    
    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int) -> None:
        self._cantidad = cantidad

    @property
    def conceptos(self) -> list['Concepto']:
        return self._conceptos

    @conceptos.setter
    def conceptos(self, conceptos: list['Concepto']):
        self._conceptos = conceptos

    @property
    def fecha_entrega(self) -> date:
        return self._fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, fecha_entrega: date):
        self._fecha_entrega = fecha_entrega
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def fecha_solicitud(self) -> date:
        return self._fecha_solicitud

    @fecha_solicitud.setter
    def fecha_solicitud(self, fecha_solicitud: date):
        self._fecha_solicitud = fecha_solicitud

    @property
    def avances(self) -> list[str]:
        return self._avances

    @avances.setter
    def avances(self, avances: list[str]):
        self._avances = avances

    @property
    def productos_finales(self) -> list[str]:
        return self._productos_finales

    @productos_finales.setter
    def productos_finales(self, productos_finales: list[str]):
        self._productos_finales = productos_finales
    
    @property
    def estado(self) -> EstadosComision:
        return self._estado

    @estado.setter
    def estado(self, estado: EstadosComision):
        self._estado = estado
    
    @property
    def pagos(self) -> list[Pago]:
        return self._pagos

    @pagos.setter
    def pagos(self, pagos: list[Pago]):
        self._pagos = pagos

    def dame_pago_total(self) -> float:
        total = 0
        for p in self.pagos:
            total += p.monto.cantidad
        return total

    def une_concepto_pago(self) -> list[tuple['Concepto', Pago]]:
        lista = []
        for c, p in zip(self.conceptos, self.pagos):
            lista.append((c,p))
        return lista
    
    def esta_pagada(self) -> bool:
        pagado = True
        if self.pagos != None:
            for p in self.pagos:
                if p.estado is not Pago.EstadoPago.PAGADO:
                    pagado = False
                    break
        else:
            pagado = False
        return pagado

#Fin clase Comision

#Inicio clase Chat
class Chat:

    def __init__(
                self, 
                artista: Usuario,  
                cliente: Usuario,
                id: int = None,
                mensajes: list[Mensaje | MensajeEstado] = [], 
                esta_deacuerdo: tuple[bool, bool] = (False, False),     #(artista, cliente)
                solicitud_cambios: bool = False,
                comision: Comision = None
                ) -> None:
        self._artista = artista
        self._cliente = cliente
        self._id = id
        self._mensajes = mensajes
        self._esta_deacuerdo = esta_deacuerdo
        self._solicitud_cambios = solicitud_cambios
        self._comision = comision

    @property
    def artista(self) -> Usuario:
        return self._artista

    @artista.setter
    def artista(self, artista: Usuario) -> None:
        self._artista = artista

    @property
    def cliente(self) -> Usuario:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: Usuario) -> None:
        self._cliente = cliente

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def mensajes(self) -> list[Mensaje]:
        return self._mensajes

    @mensajes.setter
    def mensajes(self, mensajes: list[Mensaje]) -> None:
        self._mensajes = mensajes

    @property
    def esta_deacuerdo(self) -> tuple[bool, bool]:
        return self._esta_deacuerdo

    @esta_deacuerdo.setter
    def esta_deacuerdo(self, esta_deacuerdo: tuple[bool, bool]) -> None:
        self._esta_deacuerdo = esta_deacuerdo

    @property
    def solicitud_cambios(self) -> bool:
        return self._solicitud_cambios

    @solicitud_cambios.setter
    def solicitud_cambios(self, solicitud_cambios: bool) -> None:
        self._solicitud_cambios = solicitud_cambios

    @property
    def comision(self) -> Comision:
        return self._comision

    @comision.setter
    def comision(self, comision: Comision) -> None:
        self._comision = comision
    
    def get_lista_imagenes(self) -> list[str]:
        lista = []
        for m in self.mensajes:
            if m.ruta_imagen != None:
                lista.append(m)
        return lista
        
#Fin clase chat

#Inicio clase Arte
class Arte:
    def __init__(
                self,
                artista: Usuario,
                ruta: str,
                nombre_archivo: str,
                id: int = None,
                etiquetas: list[str] = [],
                titulo: str = ''
                ) -> None:  
        
        self._artista: Usuario = artista,
        self._ruta: str = ruta,
        self._nombre_archivo: str = nombre_archivo,
        self._id: int = id
        self._etiquetas: list[str] = etiquetas
        self._titulo: str = titulo

    @property
    def artista(self) -> 'Usuario':
        return self._artista

    @artista.setter
    def artista(self, artista: 'Usuario') -> None:
        self._artista = artista

    @property
    def ruta(self) -> str:
        return self._ruta

    @ruta.setter
    def ruta(self, ruta: str) -> None:
        self._ruta = ruta

    @property
    def nombre_archivo(self) -> str:
        return self._nombre_archivo

    @nombre_archivo.setter
    def nombre_archivo(self, nombre_archivo: str) -> None:
        self._nombre_archivo = nombre_archivo

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def etiquetas(self) -> list[str]:
        return self._etiquetas

    @etiquetas.setter
    def etiquetas(self, etiquetas: list[str]) -> None:
        self._etiquetas = etiquetas

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo

#Fin clase arte

class Contacto:
    
    class TipoContacto(Enum):

        DEVIANTART = 'Deviantart'
        FACEBOOK = 'Facebook'
        INSTAGRAM = 'Instagram'
        KOFI = 'Kofi'
        PATREON = 'Patreon'
        TWITCH = 'Twitch'
        TWITTER = 'Twitter'
        YOUTUBE = 'Youtube'
        CORREO = 'E-mail'
        TELEFONO = 'Teléfono'
        OTRA = 'Link'


    def __init__(
                self, 
                usuario: Usuario,  
                tipo_contacto: TipoContacto, 
                enlace: str,
                id: int = None
                ) -> None:
        self._usuario: Usuario = usuario
        self._tipo_contacto: Contacto.TipoContacto = tipo_contacto
        self._enlace: str = enlace
        self._id: int = id
    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @usuario.setter
    def usuario(self, usuario: Usuario) -> None:
        self._usuario = usuario

    @property
    def tipo_contacto(self) -> TipoContacto:
        return self._tipo_contacto

    @tipo_contacto.setter
    def tipo_contacto(self, tipo_contacto: TipoContacto) -> None:
        self._tipo_contacto = tipo_contacto

    @property
    def enlace(self) -> str:
        return self._enlace

    @enlace.setter
    def enlace(self, enlace: str) -> None:
        self._enlace = enlace

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

#servicios: list[tuple[str, 'Dinero', bool]],    #(descripcion, precio, es_extra)
class Concepto:
    
    def __init__(
                self,
                descripcion: str,
                precio: Dinero,
                es_extra: bool,
                id: int = None
                ) -> None:
        self._descripcion: str = descripcion
        self._precio: Dinero = precio
        self._es_extra: bool = es_extra
        self._id: int = id

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        self._descripcion = descripcion

    @property
    def precio(self) -> Dinero:
        return self._precio

    @precio.setter
    def precio(self, precio: Dinero) -> None:
        self._precio = precio

    @property
    def es_extra(self) -> bool:
        return self._es_extra

    @es_extra.setter
    def es_extra(self, es_extra: bool) -> None:
        self._es_extra = es_extra

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id
                