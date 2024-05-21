from abc import ABC, abstractmethod


class ICalificacion(ABC):
    @abstractmethod
    def get_datos(self):
        pass

    @abstractmethod
    def get_estudiante(self):
        pass

    @abstractmethod
    def get_profesor(self):
        pass

    @abstractmethod
    def get_puntuacion(self):
        pass