from curso import Curso


class CursoFactory:
    @staticmethod
    def crear_curso(nombre, descripcion, profesor):
        return Curso(nombre, descripcion, profesor)