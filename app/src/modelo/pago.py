from usuario import Usuario
from dinero import Dinero
from comision import Comision
from datetime import datetime
from enum import Enum

class Pago:
    
    class EstadoPago(Enum):
        EN_PROCESO = 1 #Cuando esparamos la verificacion del pago
        PAGADO = 2 #Cuando ya se verifico al transaccion.

    def __init__(self,
                comision: Comision,
                cliente: Usuario, 
                monto: Dinero, 
                estado: EstadoPago = EstadoPago.EN_PROCESO,
                id: int = None,
                fecha_hora: datetime = datetime.now(),                
                ) -> None:
        self._comision: Comision = comision
        self._cliente: Usuario = cliente
        self._monto: Dinero = monto
        self._estado: self.EstadoPago = estado
        self._id: int = id
        self._fecha_hora: datetime = fecha_hora
        
    

   

