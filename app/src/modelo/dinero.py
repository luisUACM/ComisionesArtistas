from enum import Enum

class Dinero:

    class TipoMoneda(Enum):

        MXN = 1
        USD = 2

    DICCIONARIO_CONVERSIONES = {'USD-MNX':19.25, 
                                'MNX-USD':0.052}

    def __init__(
                self,
                moneda: TipoMoneda, 
                cantidad: float,
                id: int = None
                ) -> None:
        self._moneda: self.TipoMoneda = moneda
        self._cantidad: float = cantidad
        self._id: int = id
    
    @property
    def moneda(self) -> TipoMoneda:
        return self._moneda

    @moneda.setter
    def moneda(self, moneda: TipoMoneda) -> None:
        self._moneda = moneda

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: float) -> None:
        self._cantidad = cantidad

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id