from enum import Enum

class Dinero:

    class TipoMoneda(Enum):

        MXN = 1
        USD = 2

    DICCIONARIOS_CONVERSIONES = {'USD-MNX':19.25, 
                                'MNX-USD':0.052}

    def __init__(self,
                moneda: TipoMoneda, 
                cantidad: float,
                id: int = None
                ) -> None:
        pass
    
    # tipo_moneda
    @property
    def moneda(self):
        return self._moneda

    @moneda.setter
    def moneda(self, moneda):
        self._moneda = moneda