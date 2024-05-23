from abc import ABC, abstractmethod


class ICurso(ABC):
    def __init__(self, nombre, descripcion, profesor):
        self._nombre = nombre
        self._descripcion = descripcion
        self._profesor = profesor
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_descripcion(self):
        return self._descripcion
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    
    # Profesor solo get
    def get_profesor(self):
        return self._profesor
    
    @abstractmethod
    def get_datos(self):
        pass