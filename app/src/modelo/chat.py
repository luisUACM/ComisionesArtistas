from usuario import Usuario
from mensaje import Mensaje

class Chat:

    def __init__(self, 
                artista: Usuario, 
                cliente: Usuario, 
                mensajes: list[Mensaje]
                ) -> None:
        pass

    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, artista):
        self._artista = artista

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente