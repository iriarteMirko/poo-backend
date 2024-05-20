from usuario import Usuario
from curso import CursoFactory


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.__profesesion = profesion
        self.__centro_laboral = centro_laboral
    
    # GETTERS    
    def get_profesion(self):
        return self.__profesesion
    
    def get_centro_laboral(self):
        return self.__centro_laboral
    
    def get_datos(self):
        print(f'PROFESOR: {self.get_nombre()} {self.get_apellidos()}')
        print(f' - Correo: {self.get_correo()}')
        print(f' - Contrasena: {self.get_contrasena()}')
        print(f' - Profesion: {self.get_profesion()}')
        print(f' - Centro laboral: {self.get_centro_laboral()}')
        print(f' - Cursos: {self.get_cursos()}')
        print('\n')
    
    # SETTERS
    def set_profesion(self, nueva_profesion):
        self.__profesesion = nueva_profesion
        print('Profesion cambiada con exito.')
    
    def set_centro_laboral(self, nuevo_centro_laboral):
        self.__centro_laboral = nuevo_centro_laboral
        print('Centro laboral cambiado con exito.')
    
    def set_datos(self):
        pass
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'profesion': self.get_profesion(),
            'centro_laboral': self.get_centro_laboral(),
            'cursos': self.get_cursos()
        }
    
    def registrarse(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_correo(correo)
        self.set_contrasena(contrasena)
        self.set_profesion(profesion)
        self.set_centro_laboral(centro_laboral)
    
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