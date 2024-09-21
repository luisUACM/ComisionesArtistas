from usuario import Usuario
from mensaje import Mensaje

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