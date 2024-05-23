from abc import ABC, abstractmethod


class ICurso(ABC):
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_descripcion(self):
        return self.descripcion
    
    def obtener_profesor(self):
        return self.profesor.obtener_nombre()
    
    @abstractmethod
    def obtener_datos(self):
        pass