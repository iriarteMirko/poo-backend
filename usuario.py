from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__contrasena = contrasena
        self.cursos = []
    
    # GETTERS
    def get_nombre(self):
        return self.__nombre
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_correo(self):
        return self.__correo
    
    def get_contrasena(self):
        return self.__contrasena
    
    def get_cursos(self):
        return self.cursos
    
    @abstractmethod
    def get_datos(self):
        pass
    
    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def set_apellidos(self, nuevos_apellidos):
        self.__apellidos = nuevos_apellidos
    
    def set_correo(self, nuevo_correo):
        self.__correo = nuevo_correo
    
    def set_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
    
    def set_cursos(self, nuevos_cursos):
        self.cursos = nuevos_cursos
    
    @abstractmethod
    def set_datos(self):
        pass
    
    # METODOS
    @abstractmethod
    def enviar_datos(self):
        pass
    
    @abstractmethod
    def registrarse(self):
        pass
    
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