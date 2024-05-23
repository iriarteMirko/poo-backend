from abc import ABC, abstractmethod


class ICalificacion(ABC):
    def __init__(self, estudiante:object, profesor:object):
        self._estudiante:object = estudiante
        self._profesor:object = profesor
    
    # Estudiante solo get
    def get_estudiante(self):
        return self._estudiante
    
    def get_profesor(self):
        return self._profesor
    
    def set_profesor(self, profesor:object):
        self._profesor:object = profesor
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def get_datos(self):
        pass