from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena):
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        self._cursos = []
    
    # GETTERS
    def get_nombre(self):
        return self._nombre
    
    def get_apellidos(self):
        return self._apellidos
    
    def get_correo(self):
        return self._correo
    
    def get_contrasena(self):
        return self._contrasena
    
    def get_cursos(self):
        return [curso.nombre for curso in self._cursos]
    
    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def set_apellidos(self, nuevos_apellidos):
        self._apellidos = nuevos_apellidos
    
    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo
    
    def set_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena
    
    # METODOS    
    def iniciar_sesion(self, correo, contrasena):
        if correo == self.get_correo() and contrasena == self.get_contrasena():
            print('Sesion iniciada con exito.')
        else:
            print('Correo o contrasena incorrectos.')
    
    def recuperar_contrasena(self, correo):
        if correo == self.get_correo():
            print(f'La contrasena es: {self.get_contrasena()}')
        else:
            print('Correo incorrecto.')
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def set_datos(self):
        pass