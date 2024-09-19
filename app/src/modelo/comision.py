from usuario import Usuario
from servicio_comision import ServicioComision
from .dinero import Dinero
from chat import Chat
from datetime import date
from enum import Enum

class Comision:

    class EstadosComision(Enum):
        
        SOLICITADA = 1 #Estado en donde se espera inicar el chat.
        POR_PAGAR = 2 #Estado donde Cliente y Artista estan de acuerdo
        EN_PROCESO = 3 #Paso el pago y se inicia el desarrollo de arte.
        TERMINADA = 4 #El artista sube -> el trabajo de arte fianlizado.
        ARCHIVADA = 5 #El cliente descarga el trabajo realizado <-
        
    #Se puede hacer igual que serviciocomision, una lista de tuplas o uno individual y una lista de extras
    def __init__(self, 
                chat: Chat,
                servicio: ServicioComision,
                cantidad: int,
                precio: list[Dinero],
                fecha_entrega: date, 
                detalles: list[str] = [],
                fecha_solicitud: date = date.today,
                avances: list[str] = [],
                producto_final: list[str] = None
                ) -> None:
        self._chat: Chat = chat
        self._servicio : ServicioComision = servicio
        self._cantidad: int = cantidad 
        self._precio: list[Dinero] = precio
        self._fecha_entrega: date = fecha_entrega
        self._detalles: str = detalles
        self._fecha_solicitud: date = fecha_solicitud
        self._avances: list[str] = avances
        self._producto_final: list[str] = producto_final

    

    # precio
    @property
    def precio(self) -> list[Dinero]:
        return self._precio

    @precio.setter
    def precio(self, precio: list[Dinero]):
        self._precio = precio

    

    # titulo
    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    # fecha_entrega
    @property
    def fecha_entrega(self) -> date:
        return self._fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, fecha_entrega: date):
        self._fecha_entrega = fecha_entrega

    # detalles
    @property
    def detalles(self) -> list[str]:
        return self._detalles

    @detalles.setter
    def detalles(self, detalles: list[str]):
        self._detalles = detalles

    # fecha_solicitud
    @property
    def fecha_solicitud(self) -> date:
        return self._fecha_solicitud

    @fecha_solicitud.setter
    def fecha_solicitud(self, fecha_solicitud: date):
        self._fecha_solicitud = fecha_solicitud

    # avances
    @property
    def avances(self) -> list[str]:
        return self._avances

    @avances.setter
    def avances(self, avances: list[str]):
        self._avances = avances

    # producto_final
    @property
    def producto_final(self) -> list[str]:
        return self._producto_final

    @producto_final.setter
    def producto_final(self, producto_final: list[str]):
        self._producto_final = producto_final