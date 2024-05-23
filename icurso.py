from abc import ABC, abstractmethod


class ICurso(ABC):
    def __init__(self, nombre:str, descripcion:str, profesor:object):
        self._nombre:str = nombre
        self._descripcion:str = descripcion
        self._profesor:object = profesor
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre:str):
        self._nombre:str = nombre
    
    def get_descripcion(self):
        return self._descripcion
    
    def set_descripcion(self, descripcion:str):
        self._descripcion:str = descripcion
    
    def get_profesor(self):
        return self._profesor
    
    @abstractmethod
    def get_datos(self):
        pass