from usuario import Usuario

class Arte:
    def __init__(
                self,
                artista: Usuario,
                ruta: str,
                nombre_archivo: str,
                extension: str,
                id: int = None,
                etiquetas: list[str] = [],
                titulo: str = ''
                ) -> None:  
        
        self._artista: Usuario = artista,
        self._ruta: str = ruta,
        self._nombre_archivo: str = nombre_archivo,
        self._extension: str = extension
        self._id: int = id
        self._etiquetas: list[str] = etiquetas
        self._titulo: str = titulo

    @property
    def artista(self) -> 'Usuario':
        return self._artista

    @artista.setter
    def artista(self, artista: 'Usuario') -> None:
        self._artista = artista

    @property
    def ruta(self) -> str:
        return self._ruta

    @ruta.setter
    def ruta(self, ruta: str) -> None:
        self._ruta = ruta

    @property
    def nombre_archivo(self) -> str:
        return self._nombre_archivo

    @nombre_archivo.setter
    def nombre_archivo(self, nombre_archivo: str) -> None:
        self._nombre_archivo = nombre_archivo

    @property
    def extension(self) -> str:
        return self._extension

    @extension.setter
    def extension(self, extension: str) -> None:
        self._extension = extension
    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def etiquetas(self) -> list[str]:
        return self._etiquetas

    @etiquetas.setter
    def etiquetas(self, etiquetas: list[str]) -> None:
        self._etiquetas = etiquetas

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo