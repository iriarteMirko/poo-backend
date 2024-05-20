from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena, cursos=[]):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__contrasena = contrasena
        self.__cursos = cursos
    
    # GETTERS
    @abstractmethod
    def get_nombre(self):
        pass
    
    @abstractmethod
    def get_apellidos(self):
        pass
    
    @abstractmethod
    def get_correo(self):
        pass
    
    @abstractmethod
    def get_contrasena(self):
        pass
    
    @abstractmethod
    def get_cursos(self):
        pass
    
    @abstractmethod
    def get_datos(self):
        pass
    
    # SETTERS
    @abstractmethod
    def set_nombre(self, nuevo_nombre):
        pass
    
    @abstractmethod
    def set_apellidos(self, nuevos_apellidos):
        pass
    
    @abstractmethod
    def set_correo(self, nuevo_correo):
        pass
    
    @abstractmethod
    def set_contrasena(self, nueva_contrasena):
        pass
    
    @abstractmethod
    def set_cursos(self, nuevos_cursos):
        pass
    
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
    
    @abstractmethod
    def iniciar_sesion(self):
        pass
    
    @abstractmethod
    def recuperar_contrasena(self):
        pass
