from profesor import Profesor
from estudiante import Estudiante


class Curso:
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f'Estudiante {estudiante.get_nombre()} agregado con exito.')
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
        print(f'Estudiante {estudiante.get_nombre()} eliminado con exito.')
    
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.get_nombre())
    
    def mostrar_curso(self):
        print(f'Nombre: {self.nombre}')
        print(f'Descripcion: {self.descripcion}')
        print(f'Profesor: {Profesor.get_nombre()}')
        print('Estudiantes:')
        self.mostrar_estudiantes()


class CursoFactory:
    @staticmethod
    def crear_curso(nombre, descripcion, profesor):
        return Curso(nombre, descripcion, profesor)