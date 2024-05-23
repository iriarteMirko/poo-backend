from icurso import ICurso


class Curso(ICurso):
    def __init__(self, nombre:str, descripcion:str, profesor:object):
        super().__init__(nombre, descripcion, profesor)
        self._estudiantes:list = []
        self._horarios:list = []
    
    def __repr__(self):
        return (f'Curso(nombre={self.get_nombre()}, descripcion={self.get_descripcion()}, Profesor={self.get_profesor().get_nombre()}, estudiantes={[estudiante.get_nombre() for estudiante in self.get_estudiantes()]}, horarios={[horario.get_datos() for horario in self.get_horarios()]})')
    
    def get_datos(self):
        return {
            'nombre': self.get_nombre(),
            'descripcion': self.get_descripcion(),
            'profesor': self.get_profesor(),
            'estudiantes': [estudiante.get_nombre() for estudiante in self.get_estudiantes()],
            'horarios': [horario.get_datos() for horario in self.get_horarios()]
        }
    
    def get_estudiantes(self):
        return self._estudiantes
    
    def get_horarios(self):
        return self._horarios
    
    def agregar_estudiante(self, estudiante:object):
        self._estudiantes.append(estudiante)
    
    def retirar_estudiante(self, estudiante:object):
        self._estudiantes.remove(estudiante)
    
    def agregar_horario(self, horario:object):
        self._horarios.append(horario)
    
    def eliminar_horario(self, horario:object):
        self._horarios.remove(horario)