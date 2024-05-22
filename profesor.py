from usuario import Usuario
from fabrica_curso import FabricaCurso
from fabrica_horario import FabricaHorario


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.profesion = profesion
        self.centro_laboral = centro_laboral
        self.puntuaciones = []
    
    def __repr__(self):
        return f'Profesor({self.obtener_nombre()}, {self.obtener_apellidos()}, {self.obtener_correo()}, {self.obtener_contrasena()}, {self.profesion}, {self.centro_laboral}), {self.obtener_cursos()}, {self.obtener_puntuacion()}'
    
    # GETTERS
    def obtener_datos(self):
        return {
            'nombre': self.obtener_nombre(),
            'apellidos': self.obtener_apellidos(),
            'correo': self.obtener_correo(),
            'profesion': self.profesion,
            'centro_laboral': self.centro_laboral,
            'cursos': self.obtener_cursos(),
            'puntuacion': self.obtener_puntuacion()
        }
    
    def obtener_puntuacion(self):
        if self.puntuaciones:
            return sum(self.puntuaciones) / len(self.puntuaciones)
        return 0
    
    # SETTERS
    def modificar_datos(self, **kwargs):
        self.modificar_nombre(kwargs.get('nombre', self.obtener_nombre()))
        self.modificar_apellidos(kwargs.get('apellidos', self.obtener_apellidos()))
        self.modificar_correo(kwargs.get('correo', self.obtener_correo()))
        self.modificar_contrasena(kwargs.get('contrasena', self.obtener_contrasena()))
        self.profesion = kwargs.get('profesion', self.profesion)
        self.centro_laboral = kwargs.get('centro_laboral', self.centro_laboral)
    
    # CURSO
    def crear_curso(self, nombre, descripcion):
        if any(curso.nombre == nombre for curso in self._cursos):
            print(f'Error: Ya existe un curso con el nombre "{nombre}".')
            return None
        
        factory = FabricaCurso()
        curso = factory.crear_curso(nombre, descripcion, self)
        self._cursos.append(curso)
        print(f'Curso {curso.nombre} creado con exito.')
        return curso
    
    def modificar_curso(self, curso, nombre=None, descripcion=None):
        if curso in self._cursos:
            if nombre:
                curso.nombre = nombre
            if descripcion:
                curso.descripcion = descripcion
            print(f'Curso modificado con éxito.')
        else:
            print(f'No se puede modificar curso, el profesor no esta asignado al curso {curso.nombre}.')
    
    def eliminar_curso(self, curso):
        if curso in self._cursos:
            self._cursos.remove(curso)
            for estudiante in curso.estudiantes:
                estudiante.retirar_curso(curso)
            print(f'Curso "{curso.nombre}" eliminado con éxito.')
        else:
            print(f'No se puede eliminar curso, el profesor no esta asignado al curso {curso.nombre}.')
    
    # ESTUDIANTES
    def ver_estudiantes(self):
        lista_estudiantes = []
        for curso in self._cursos:
            for estudiante in curso.estudiantes:
                lista_estudiantes.append(estudiante.obtener_nombre()+'('+curso.nombre+')')
        return lista_estudiantes
    
    # HORARIO
    def crear_horario(self, curso, dia, hora_inicio, hora_fin):
        if curso in self._cursos:
            factory = FabricaHorario()
            horario = factory.crear_horario(curso, dia, hora_inicio, hora_fin)
            curso.horarios.append(horario)
            print(f'Horario creado con exito.')
            return horario
        else:
            print(f'No se puede crear horario, el profesor no esta asignado al curso {curso.nombre}.')
            return None
    
    def modificar_horario(self, curso, horario, dia=None, hora_inicio=None, hora_fin=None):
        if curso in self._cursos:
            if horario in curso.horarios:
                if dia:
                    horario.dia = dia
                if hora_inicio:
                    horario.hora_inicio = hora_inicio
                if hora_fin:
                    horario.hora_fin = hora_fin
                print('Horario modificado con exito.')
            else:
                print(f'No se puede modificar horario, el horario no pertenece al curso {curso.nombre}.')
        else:
            print(f'No se puede modificar horario, el profesor no esta asignado al curso {curso.nombre}.')
    
    def eliminar_horario(self, curso, horario):
        if curso in self._cursos:
            if horario in curso.horarios:
                curso.horarios.remove(horario)
                print('Horario eliminado con exito.')
            else:
                print(f'No se puede eliminar horario, el horario no pertenece al curso {curso.nombre}.')
        else:
            print(f'No se puede eliminar horario, el profesor no esta asignado al curso {curso.nombre}.')
    
    # RECIBIR CALIFICACIÓN
    def recibir_calificacion(self, puntuacion):
        self.puntuaciones.append(puntuacion)