from icurso import ICurso


class Curso(ICurso):
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
        self.estudiantes = []
        self.horarios = []
    
    def get_datos(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'profesor': self.get_profesor(),
            'estudiantes': self.get_estudiantes()
        }
    
    def get_estudiantes(self):
        return [estudiante.get_nombre() for estudiante in self.estudiantes]
    
    def get_profesor(self):
        return self.profesor.get_nombre() + ' ' + self.profesor.get_apellidos()
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
    
