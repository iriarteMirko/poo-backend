from abc import ABC, abstractmethod


class ICalificacion(ABC):
    def __init__(self, estudiante, profesor):
        self.estudiante = estudiante
        self.profesor = profesor
    
    # PROPIEDADES
    @property
    def estudiante(self):
        return self.estudiante
    
    @property
    def profesor(self):
        return self.profesor
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def obtener_datos(self):
        pass