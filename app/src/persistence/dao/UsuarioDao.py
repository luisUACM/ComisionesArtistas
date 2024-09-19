from ..db_helper import get_conexion
from ..db_helper import cerrar_conexion
from ...modelo.usuario import Usuario

class UsuarioDao:

    def guardar(self, usuario: Usuario):
        if self.get(usuario.id) is not None:
            self.actualizar()
        else:
            conexion = get_conexion()
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuarios (correo, contrasena) VALUES (?, ?)', (usuario.correo, usuario.contrasena))
            conexion.commit()
            cerrar_conexion()
    
    def get(self, id: int) -> Usuario:
        pass

    def actualizar(usuario: Usuario):
        pass

    def borrar():
        pass