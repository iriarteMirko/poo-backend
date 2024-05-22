from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena):
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        self._cursos = []
    
    # GETTERS
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_apellidos(self):
        return self._apellidos
    
    def obtener_correo(self):
        return self._correo
    
    def obtener_contrasena(self):
        return self._contrasena
    
    def obtener_cursos(self):
        return [curso.nombre for curso in self._cursos]
    
    # SETTERS
    def modificar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def modificar_apellidos(self, nuevos_apellidos):
        self._apellidos = nuevos_apellidos
    
    def modificar_correo(self, nuevo_correo):
        self._correo = nuevo_correo
    
    def modificar_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena
    
    # METODOS
    def iniciar_sesion(self, correo, contrasena):
        if correo == self.obtener_correo() and contrasena == self.obtener_contrasena():
            print('Sesion iniciada con exito.')
        else:
            print('Correo o contrasena incorrectos.')
    
    def recuperar_contrasena(self, correo):
        if correo == self.obtener_correo():
            print(f'La contrasena es: {self.obtener_contrasena()}')
        else:
            print('Correo incorrecto.')
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def obtener_datos(self):
        pass
    
    @abstractmethod
    def modificar_datos(self):
        pass