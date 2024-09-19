from usuario import Usuario

class Arte:
    def __init__(self,
                artista: Usuario,
                ruta: str,
                nombre_archivo: str,
                extension: str,
                id: int = None,
                etiquetas: list[str] = None,
                titulo: str = '' 
                ) -> None:  
        self._id : int = id
        self._artista : Usuario = artista,
        self._ruta : str = ruta,
        self._nombre: str = nombre_archivo,
        self._etiquetas = list[str] = etiquetas