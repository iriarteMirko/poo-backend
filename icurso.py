from abc import ABC, abstractmethod


class ICurso(ABC):
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
    
    # PROPIEDADES
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def descripcion(self):
        return self.descripcion
    
    @property
    def profesor(self):
        return self.profesor
    
    # METODOS
    @abstractmethod
    def obtener_datos(self):
        pass