class Usuario:

    def __init__(self, id: int = None, correo: str = None, contrasena: str = None ) -> None:
        self._id: int = id
        self._correo: str = correo
        self._contrasena: str = contrasena

    #Getter

    @property
    def id(self) -> str:
        return self._id
    
    #Setter
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def correo(self) -> str:
        return self._correo
    
    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self) -> str:
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena
    