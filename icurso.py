from abc import ABC, abstractmethod


class ICurso(ABC):
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def get_profesor(self):
        pass
    
    @abstractmethod
    def get_estudiantes(self):
        pass
    
    @abstractmethod
    def get_horarios(self):
        pass