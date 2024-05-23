from abc import ABC, abstractmethod


class FabricaCursosAbstracta(ABC):
    @abstractmethod
    def crear_curso():
        pass


class FabricaHorariosAbstracta(ABC):
    @abstractmethod
    def crear_horario():
        pass
