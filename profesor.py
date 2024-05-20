from usuario import Usuario
from curso_factory import CursoFactory


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.profesesion = profesion
        self.centro_laboral = centro_laboral
    
    # GETTERS
    def get_datos(self):
        print(f'PROFESOR: {self.get_nombre()} {self.get_apellidos()}')
        print(f' - Correo: {self.get_correo()}')
        print(f' - Contrasena: {self.get_contrasena()}')
        print(f' - Profesion: {self.profesesion}')
        print(f' - Centro laboral: {self.centro_laboral}')
        print(f' - Cursos: {self.cursos}')
    
    # SETTERS
    def set_datos(self, nuevo_nombre, nuevos_apellidos, nuevo_correo, nueva_contrasena, nueva_profesion, nuevo_centro_laboral): 
        self.set_nombre(nuevo_nombre)
        self.set_apellidos(nuevos_apellidos)
        self.set_correo(nuevo_correo)
        self.set_contrasena(nueva_contrasena)
        self.profesesion = nueva_profesion
        self.centro_laboral = nuevo_centro_laboral
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'profesion': self.profesesion,
            'centro_laboral': self.centro_laboral,
            'cursos': self.cursos
        }
    
    def registrarse(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_correo(correo)
        self.set_contrasena(contrasena)
        self.profesesion = profesion
        self.centro_laboral = centro_laboral
    
    # CURSO
    def crear_curso(self, nombre, descripcion):
        factory = CursoFactory()
        curso = factory.crear_curso(nombre, descripcion, self)
        self.cursos.append(curso)
        print(f'Curso {curso.nombre} creado con exito.')
        return curso
    
    def modificar_curso(self, curso, nombre=None, descripcion=None):
        if nombre:
            curso.nombre = nombre
        if descripcion:
            curso.descripcion = descripcion
        print(f'Curso {curso.nombre} modificado con exito.')
    
    def eliminar_curso(self, curso):
        self.cursos.remove(curso)
        print(f'Curso {curso.nombre} eliminado con exito.')
    
    # HORARIO
    def crear_horario(self):
        pass
    
    def modificar_horario(self):
        pass
    
    def eliminar_horario(self):
        pass
    
    def ver_horario(self):
        pass
    
    # ESTUDIANTES
    def ver_estudiantes(self):
        pass
    
    # NOTIFICACIONES
    def enviar_notificacion(self):
        pass