from src.modelo.dinero import Dinero
from src.modelo.arte import Arte

class ServicioComision:

    def __init__(self, 
                titulo: str, 
                #precio: Dinero, 
                arte_promocional: list[Arte],
                contrato: list[str],
                id: int = None,
                #descripcion: str = '',
                extras: list[tuple[str, Dinero]] = []
                ) -> None:
        pass