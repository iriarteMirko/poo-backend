from abc import ABC, abstractmethod


class ICalificacion(ABC):
    def __init__(self, estudiante, profesor):
        self._estudiante = estudiante
        self._profesor = profesor
    
    # Estudiante solo get
    def get_estudiante(self):
        return self._estudiante
    
    def get_profesor(self):
        return self._profesor
    
    def set_profesor(self, profesor):
        self._profesor = profesor
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def get_datos(self):
        pass