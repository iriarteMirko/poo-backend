from icurso import ICurso


class Curso(ICurso):
    def __init__(self, nombre, descripcion, profesor):
        super().__init__(nombre, descripcion, profesor)
        self.estudiantes = []
        self.horarios = []
    
    def __repr__(self):
        return f'Curso({self.obtener_nombre()}, {self.obtener_descripcion()}, {self.obtener_profesor()}, {self.obtener_estudiantes()}, {self.obtener_horarios()})'
    
    def obtener_datos(self):
        return {
            'nombre': self.obtener_nombre(),
            'descripcion': self.obtener_descripcion(),
            'profesor': self.obtener_profesor(),
            'estudiantes': self.obtener_estudiantes(),
            'horarios': self.obtener_horarios()
        }
    
    def obtener_estudiantes(self):
        return [estudiante.obtener_nombre() for estudiante in self.estudiantes]
    
    def obtener_horarios(self):
        return [horario.obtener_datos() for horario in self.horarios]
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
    
    def agregar_horario(self, horario):
        self.horarios.append(horario)
    
    def eliminar_horario(self, horario):
        self.horarios.remove(horario)