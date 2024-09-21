from src.modelo.dinero import Dinero
from src.modelo.arte import Arte

class ServicioComision:

    def __init__(
                self, 
                titulo: str, 
                servicios: list[tuple[str, Dinero, bool]],    #(descripcion, precio, es_extra)
                piezas_arte: list[Arte],
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
    def servicios(self) -> list[tuple[str, Dinero, bool]]:
        return self._servicios

    @servicios.setter
    def servicios(self, servicios: list[tuple[str, Dinero, bool]]) -> None:
        self._servicios = servicios

    @property
    def piezas_arte(self) -> list[Arte]:
        return self._piezas_arte

    @piezas_arte.setter
    def piezas_arte(self, piezas_arte: list[Arte]) -> None:
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