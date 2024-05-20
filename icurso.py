from abc import ABC, abstractmethod


class ICurso(ABC):
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def agregar_estudiante(self, estudiante):
        pass
    
    @abstractmethod
    def eliminar_estudiante(self, estudiante):
        pass
    
    @abstractmethod
    def get_estudiantes(self):
        pass
    
    @abstractmethod
    def get_profesor(self):
        pass