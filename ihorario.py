from abc import ABC, abstractmethod


class IHorario(ABC):
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def get_curso(self):
        pass