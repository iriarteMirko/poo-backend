from abc import ABC, abstractmethod


class IHorario(ABC):
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def modificar_horario(self, dia=None, hora_inicio=None, hora_fin=None):
        pass
    
    @abstractmethod
    def eliminar_horario(self):
        pass
    
    @abstractmethod
    def get_curso(self):
        pass