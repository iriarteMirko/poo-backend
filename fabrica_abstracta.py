from abc import ABC, abstractmethod


class FabricaCursosAbstracta(ABC):
    @abstractmethod
    def crear_curso(self, nombre, descripcion, profesor):
        pass


class FabricaHorariosAbstracta(ABC):
    @abstractmethod
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        pass
