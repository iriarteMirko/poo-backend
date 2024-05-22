from fabrica_abstracta import FabricaCursosAbstracta
from curso import Curso


class FabricaCurso(FabricaCursosAbstracta):
    @staticmethod
    def crear_curso(nombre, descripcion, profesor):
        return Curso(nombre, descripcion, profesor)