from abc import ABC, abstractmethod


class ICurso(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass
    
    @abstractmethod
    def obtener_profesor(self):
        pass
    
    @abstractmethod
    def obtener_estudiantes(self):
        pass
    
    @abstractmethod
    def obtener_horarios(self):
        pass