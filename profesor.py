from usuario import Usuario
from curso_factory import CursoFactory


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.profesion = profesion
        self.centro_laboral = centro_laboral
    
    # GETTERS
    def get_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'profesion': self.profesion,
            'centro_laboral': self.centro_laboral,
            'cursos': self.get_cursos()
        }
    
    # SETTERS
    def set_datos(self, **kwargs):
        self.set_nombre(kwargs.get('nombre', self.get_nombre()))
        self.set_apellidos(kwargs.get('apellidos', self.get_apellidos()))
        self.set_correo(kwargs.get('correo', self.get_correo()))
        self.set_contrasena(kwargs.get('contrasena', self.get_contrasena()))
        self.profesion = kwargs.get('profesion', self.profesion)
        self.centro_laboral = kwargs.get('centro_laboral', self.centro_laboral)
    
    # CURSO
    def crear_curso(self, nombre, descripcion):
        factory = CursoFactory()
        curso = factory.crear_curso(nombre, descripcion, self)
        self._cursos.append(curso)
        print(f'Curso {curso.nombre} creado con exito.')
        return curso
    
    def modificar_curso(self, curso, nombre=None, descripcion=None):
        if nombre:
            curso.nombre = nombre
        if descripcion:
            curso.descripcion = descripcion
        print(f'Curso {curso.nombre} modificado con exito.')
    
    def eliminar_curso(self, curso):
        self._cursos.remove(curso)
        print(f'Curso {curso.nombre} eliminado con exito.')
    
    # ESTUDIANTES
    def ver_estudiantes(self):
        lista_estudiantes = []
        for curso in self._cursos:
            for estudiante in curso.estudiantes:
                lista_estudiantes.append(estudiante.get_nombre()+ ' del curso: ' + curso.nombre)
        return lista_estudiantes
    
    # HORARIO
    def crear_horario(self):
        pass
    
    def modificar_horario(self):
        pass
    
    def eliminar_horario(self):
        pass
    
    def ver_horario(self):
        pass
    
    # NOTIFICACIONES
    def enviar_notificacion(self):
        pass