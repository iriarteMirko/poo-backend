class Curso:
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
        self.estudiantes = []
        self.horarios = []
    
    def __repr__(self):
        return f'Curso({self.nombre}, {self.descripcion}, {self.obtener_profesor()}, {self.obtener_estudiantes()}, {self.obtener_horarios()})'
    
    def obtener_datos(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'profesor': self.obtener_profesor(),
            'estudiantes': self.obtener_estudiantes(),
            'horarios': self.obtener_horarios()
        }
    
    def obtener_profesor(self):
        return self.profesor.obtener_nombre() + ' ' + self.profesor.obtener_apellidos()
    
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