from fabrica_abstracta import FabricaCursosAbstracta
from curso import Curso


class FabricaCurso(FabricaCursosAbstracta):
    @staticmethod
    def crear_curso(nombre:str, descripcion:str, profesor:object):
        return Curso(nombre, descripcion, profesor)