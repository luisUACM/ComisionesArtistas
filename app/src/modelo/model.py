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
        self._moneda: self.TipoMoneda = moneda
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
                rol: list[Rol],
                contrasena: str, 
                nombre: str, 
                disponible:bool =True, #Nuevo atributo 
                id: int = None, 
                biografia: str = '',
                foto_perfil: str = '/fotos_perfil/generic.webp',
                moneda: Dinero.TipoMoneda = Dinero.TipoMoneda.MXN,
                portafolio: list['Arte'] = [],     
                comisiones: list['Comision'] = [], 
                servicios: list['Servicio'] = [],  
                contactos: list['Contacto'] = []   
                ) -> None:
        
        self._correo: str = correo
        self._contrasena: str = contrasena
        self._nombre: str = nombre
        self._rol: list[self.Rol] = rol
        self._id: int = id
        self._biografia: str = biografia
        self._foto_perfil: str = foto_perfil
        self._moneda: Dinero.TipoMoneda = moneda
        self._portafolio: list[Arte] = portafolio
        self._comisiones: list[Comision] = comisiones
        self._servicios: list[Servicio] = servicios
        self._contactos: list[Contacto] = contactos

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
    def rol(self) -> list[Rol]:
        return self._rol
    
    @rol.setter
    def rol(self, rol: list[Rol]):
        self._rol = rol

    @property
    def disponible(self) -> bool:
        return self._disponible
    
    @rol.setter
    def disponible(self, disponible: bool):
        self._disponible = disponible

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
    
    def esta_disponible() -> bool:
        pass

#Fin clase usuario

#CLASE Servicio
class Servicio:
    def __init__(
                self, 
                titulo: str, 
                conceptos: list['Concepto'],  
                piezas_arte: list['Arte'],
                contrato: list[str],
                id: int = None,
                artista: Usuario = None
             

                ) -> None:
        self._titulo = titulo
        self._conceptos = conceptos
        self._piezas_arte = piezas_arte
        self._contrato = contrato
        self._id = id
        self._artista = artista

    def obtener_ruta_primera_arte(self) -> str:
        if self._piezas_arte:
            return self._piezas_arte[0].ruta  # Retorna la ruta de la primera obra de arte
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
    def contrato(self) -> list[str]:
        return self._contrato

    @contrato.setter
    def contrato(self, contrato: list[str]) -> None:
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
        self._estado: self.EstadoPago = estado
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
                chat: 'Chat' = None    
                ) -> None:
        self._usuario = usuario
        self._mensaje = mensaje
        self._id: int = id
        self._fecha_hora = fecha_hora

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

#Fin clase mensaje

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
                servicio: Servicio,
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
        self._servicio : Servicio = servicio
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
        return self._servicio

    @servicio.setter
    def servicio(self, servicio: 'Chat') -> None:
        self._servicio = servicio
    
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

#Fin clase Comision

#Inicio clase Chat
class Chat:

    def __init__(
                self, 
                artista: Usuario,  
                cliente: Usuario,  
                mensajes: list[Mensaje] = [],  
                esta_deacuerdo: tuple[bool, bool] = (False, False),     #(artista, cliente)
                solicitud_cambios: bool = False
                ) -> None:
        self._artista = artista
        self._cliente = cliente
        self._mensajes = mensajes
        self._esta_deacuerdo = esta_deacuerdo
        self._solicitud_cambios = solicitud_cambios

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
                