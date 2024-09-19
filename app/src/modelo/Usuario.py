from enum import Enum
from comision import Comision
from src.modelo.arte import Arte

class Usuario:

    class Rol(Enum):

        ARTISTA = 1
        CLIENTE = 2

    def __init__(self, 
                correo: str, 
                contrasena: str, 
                nombre: str, 
                rol: Rol, 
                id: int = None, 
                portafolio: list[Arte] = [],
                lista_comisiones: list[Comision] = []
                ) -> None:
        self._id: int = id
        self._correo: str = correo
        self._contrasena: str = contrasena
        self._nombre: str = nombre
        self._rol: self.Rol = rol
        self._portafolio: list[str] = portafolio
        self._lista_comisiones: list[Comision] = lista_comisiones
    
    #Getter
    
    @property
    def id(self) -> str:
        return self._id
    
    #Setter
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def correo(self) -> str:
        return self._correo
    
    @correo.setter
    def correo(self, correo: str):
        self._correo = correo

    @property
    def contrasena(self) -> str:
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, contrasena: str):
        self._contrasena = contrasena
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, rol: Rol):
        self._rol = rol
    
    @property
    def lista_comisiones(self) -> list[Comision]:
        return self._lista_comisiones
    
    @lista_comisiones.setter
    def lista_comisiones(self, lista_comisiones: list[Comision]):
        self._lista_comisiones = lista_comisiones

    @property
    def portafolio(self) -> list[str]:
        return self._portafolio
    
    @portafolio.setter
    def portafolio(self, portafolio: list[str]):
        self._portafolio = portafolio