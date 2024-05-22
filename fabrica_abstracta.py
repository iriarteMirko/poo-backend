from abc import ABC, abstractmethod


class FabricaAbstracta(ABC):
    @abstractmethod
    def crear_curso(self, nombre, descripcion, profesor):
        pass

    @abstractmethod
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        pass
