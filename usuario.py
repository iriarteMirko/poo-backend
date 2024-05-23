from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre:str, apellidos:str, correo:str, contrasena:str):
        self._nombre:str = nombre
        self._apellidos:str = apellidos
        self._correo:str = correo
        self._contrasena:str = contrasena
        self._cursos:list = []
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre:str):
        self._nombre:str = nuevo_nombre
    
    def get_apellidos(self):
        return self._apellidos
    
    def set_apellidos(self, nuevos_apellidos:str):
        self._apellidos:str = nuevos_apellidos
    
    def get_correo(self):
        return self._correo
    
    def set_correo(self, nuevo_correo:str):
        self._correo:str = nuevo_correo
    
    def get_contrasena(self):
        return self._contrasena
    
    def set_contrasena(self, nueva_contrasena:str):
        self._contrasena:str = nueva_contrasena
    
    def get_cursos(self):
        return self._cursos
    
    def iniciar_sesion(self, correo:str, contrasena:str):
        if correo == self.get_correo() and contrasena == self.get_contrasena():
            print('Sesion iniciada con exito.')
        else:
            print('Correo o contrasena incorrectos.')
    
    def recuperar_contrasena(self, correo:str):
        if correo == self.get_correo():
            print(f'La contrasena es: {self.get_contrasena()}')
        else:
            print('Correo incorrecto.')
    
    def agregar_curso(self, curso:object):
        self._cursos.append(curso)
    
    def quitar_curso(self, curso:object):
        self._cursos.remove(curso)
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def modificar_datos(self):
        pass