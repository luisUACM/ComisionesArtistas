from usuario import Usuario
from dinero import Dinero
from comision import Comision
from datetime import datetime
from enum import Enum

class Pago:
    
    class EstadoPago(Enum):
        
        EN_PROCESO = 1 #Cuando esperamos la verificacion del pago
        PAGADO = 2 #Cuando ya se verifico al transaccion.
        PENDIENTE = 3 #No se ha pagado por cualquier motivo

    def __init__(
                self,
                comision: Comision,
                cliente: Usuario, 
                monto: Dinero, 
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
    def comision(self) -> Comision:
        return self._comision

    @comision.setter
    def comision(self, comision: Comision) -> None:
        self._comision = comision

    @property
    def cliente(self) -> Usuario:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: Usuario) -> None:
        self._cliente = cliente

    @property
    def monto(self) -> Dinero:
        return self._monto

    @monto.setter
    def monto(self, monto: Dinero) -> None:
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
        
    

   

