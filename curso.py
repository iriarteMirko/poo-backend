from icurso import ICurso


class Curso(ICurso):
    def __init__(self, nombre, descripcion, profesor):
        super().__init__(nombre, descripcion, profesor)
        self.estudiantes = []
        self.horarios = []
    
    def __repr__(self):
        return (f'Curso({self.nombre}, {self.descripcion}, {self.profesor.nombre}, 
                {[estudiante.nombre for estudiante in self.estudiantes]}, 
                {[horario.obtener_datos() for horario in self.horarios]})')
    
    # PROPIEDADES
    @property
    def estudiantes(self):
        return self.estudiantes
    
    @property
    def horarios(self):
        return self.horarios
    
    # METODOS
    def obtener_datos(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'profesor': self.profesor,
            'estudiantes': self.estudiantes,
            'horarios': self.horarios
        }
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
    
    def agregar_horario(self, horario):
        self.horarios.append(horario)
    
    def eliminar_horario(self, horario):
        self.horarios.remove(horario)