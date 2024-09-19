from usuario import Usuario
from datetime import datetime

class Mensaje:
    
    def __init__(self, 
                usuario: Usuario, 
                mensaje: str,
                id: int = None,
                fecha_hora: datetime = datetime.now(), 
                ) -> None:
        pass