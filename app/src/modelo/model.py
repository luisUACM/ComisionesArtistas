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
                contrasena: str, 
                nombre: str, 
                rol: Rol, 
                #PK
                id: int = None, 
                #FK
                portafolio: list['Arte'] = [],
                #FK
                comisiones: list['Comision'] = [],
                servicios: list['Servicio'] = [],
                biografia: str = '',
                foto_perfil: str = '',
                contactos: list['Contacto'] = [],
                moneda: Dinero.TipoMoneda = Dinero.TipoMoneda.MXN
                ) -> None:
        
        self._correo: str = correo
        self._contrasena: str = contrasena
        self._nombre: str = nombre
        self._rol: self.Rol = rol
        self._id: int = id
        self._portafolio: list[str] = portafolio
        self._comisiones: list[Comision] = comisiones
        self._biografia: str = biografia
        self._foto_perfil: str = foto_perfil
        self._redes_sociales: list[tuple[self.RedSocial, str]] = redes_sociales     #(red_social, link)
        self._moneda: Dinero.TipoMoneda = moneda

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
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, rol: Rol):
        self._rol = rol

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id
    
    @property
    def comisiones(self) -> list['Servicio']:
        return self._comisiones
    
    @comisiones.setter
    def comisiones(self, comisiones: list['Servicio']):
        self._comisiones = comisiones

    @property
    def portafolio(self) -> list[str]:
        return self._portafolio
    
    @portafolio.setter
    def portafolio(self, portafolio: list[str]):
        self._portafolio = portafolio
    
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
    def redes_sociales(self) -> list[tuple[RedSocial, str]]:
        return self._redes_sociales
    
    @redes_sociales.setter
    def redes_sociales(self, redes_sociales: list[tuple[RedSocial, str]]):
        self._redes_sociales = redes_sociales

    @property
    def moneda(self) -> str:
        return self.moneda
    
    @moneda.setter
    def moneda(self, moneda: str):
        self.moneda = moneda

#Fin clase usuario

#CLASE ServicioComision
class Servicio:
    def __init__(
                self, 
                titulo: str, 
                #FK
                conceptos: list['Concepto'],
                piezas_arte: list['Arte'],
                contrato: list[str],
                id: int = None,
                ) -> None:
        self._titulo = titulo
        self._servicios = servicios
        self._piezas_arte = piezas_arte
        self._contrato = contrato
        self._id = id
    
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo

    @property
    def servicios(self) -> list[tuple[str, 'Dinero', bool]]:
        return self._servicios

    @servicios.setter
    def servicios(self, servicios: list[tuple[str, 'Dinero', bool]]) -> None:
        self._servicios = servicios

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

#Fin clase servicio_comision

#Inicio clase Pago
class Pago:
    
    class EstadoPago(Enum):
        
        EN_PROCESO = 1 #Cuando esperamos la verificacion del pago
        PAGADO = 2 #Cuando ya se verifico al transaccion.
        PENDIENTE = 3 #No se ha pagado por cualquier motivo

    def __init__(
                self,
                #FK
                comision: 'Comision',
                #FK
                cliente: 'Usuario', 
                #FK
                monto: 'Dinero', 
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
                productos_finales: list[str] = None,
                estado: EstadosComision = EstadosComision.SOLICITADA
                ) -> None:
        self._chat: Chat = chat
        self._servicio : Servicio = servicio
        self._cantidad: int = cantidad 
        self._precio: list[Dinero] = precio
        self._detalles: str = detalles
        self._fecha_entrega: date = fecha_entrega
        self._id: int = id
        self._fecha_solicitud: date = fecha_solicitud
        self._avances: list[str] = avances
        self._producto_final: list[str] = productos_finales

    @property
    def precio(self) -> list[Dinero]:
        return self._precio

    @precio.setter
    def precio(self, precio: list[Dinero]):
        self._precio = precio    

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def detalles(self) -> list[str]:
        return self._detalles

    @detalles.setter
    def detalles(self, detalles: list[str]):
        self._detalles = detalles

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
    def producto_final(self) -> list[str]:
        return self._producto_final

    @producto_final.setter
    def producto_final(self, producto_final: list[str]):
        self._producto_final = producto_final

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
                id_artista: int,
                ruta: str,
                nombre_archivo: str,
                extension: str,
                id: int = None,
                etiquetas: list[str] = [],
                titulo: str = ''
                ) -> None:  
        
        self._artista: Usuario = artista,
        self._ruta: str = ruta,
        self._nombre_archivo: str = nombre_archivo,
        self._extension: str = extension
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
    def extension(self) -> str:
        return self._extension

    @extension.setter
    def extension(self, extension: str) -> None:
        self._extension = extension
    
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

#----------------------Clases nuevas----------------------#
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
                id_usuario: int,
                tipo_contacto: TipoContacto, 
                enlace: str,
                id: int = None
                ) -> None:
        pass

#servicios: list[tuple[str, 'Dinero', bool]],    #(descripcion, precio, es_extra)
class Concepto:
    
    def __init__(
                self,
                descripcion: str,
                precio: Dinero,
                es_extra: bool,
                id: int = None
                ) -> None:
        pass
                
"""
ATRIBUTOS AGREGADOS

Comision 
    -> estado
    -> producto_final se renombro a productos_finales
Arte -> id_artista
ServicioComision 
    -> id_artista
    -> servicios se cambio a conceptos y de tipo Concepto
Usuario    
    -> redes_sociales se renombro a contactos y cambio el tipo
    -> portafolio es FK
    -> servicios es FK
    -> comisiones es FK
Chat
    -> falta id
"""