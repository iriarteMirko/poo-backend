from abc import ABC, abstractmethod


class IHorario(ABC):
    def __init__(self, curso:object):
        self._curso:object = curso
    
    # Curso solo get
    def get_curso(self):
        return self._curso.get_nombre()
    
    @abstractmethod
    def get_datos(self):
        pass