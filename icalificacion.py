from abc import ABC, abstractmethod


class ICalificacion(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass
    
    @abstractmethod
    def obtener_estudiante(self):
        pass
    
    @abstractmethod
    def obtener_puntuacion(self):
        pass