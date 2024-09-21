from usuario import Usuario
from datetime import datetime

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
        self._id = id
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