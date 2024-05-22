from abc import ABC, abstractmethod


class IHorario(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass
    
    @abstractmethod
    def obtener_curso(self):
        pass