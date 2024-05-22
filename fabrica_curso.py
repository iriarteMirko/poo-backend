from curso import Curso
from fabrica_abstracta import FabricaAbstracta


class FabricaCurso(FabricaAbstracta):
    @staticmethod
    def crear_curso(nombre, descripcion, profesor):
        return Curso(nombre, descripcion, profesor)