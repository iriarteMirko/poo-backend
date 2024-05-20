from usuario import Usuario
from curso import CursoFactory


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, cursos, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena, cursos)
        self.profesesion = profesion
        self.centro_laboral = centro_laboral
    
    # GETTERS
    def get_nombre(self):
        return self.__nombre
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_correo(self):
        return self.__correo
    
    def get_contrasena(self):
        return self.__contrasena
    
    def get_cursos(self):
        return self.__cursos
    
    def get_profesion(self):
        return self.profesesion
    
    def get_centro_laboral(self):
        return self.centro_laboral
    
    def get_cursos(self):
        return self.cursos
    
    def get_datos(self):
        print(f'Nombre: {self.get_nombre()}')
        print(f'Apellidos: {self.get_apellidos()}')
        print(f'Correo: {self.get_correo()}')
        print(f'Contrasena: {self.get_contrasena()}')
        print(f'Profesion: {self.get_profesion()}')
        print(f'Centro laboral: {self.get_centro_laboral()}')
        print(f'Cursos: {self.get_cursos()}')
    
    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        print('Nombre cambiado con exito.')
    
    def set_apellidos(self, nuevos_apellidos):
        self.__apellidos = nuevos_apellidos
        print('Apellidos cambiados con exito.')
    
    def set_correo(self, nuevo_correo):
        self.__correo = nuevo_correo
        print('Correo cambiado con exito.')
    
    def set_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        print('Contrasena cambiada con exito.')
    
    def set_cursos(self, nuevos_cursos):
        self.__cursos = nuevos_cursos
        print('Cursos cambiados con exito.')
    
    def set_profesion(self, nueva_profesion):
        self.profesesion = nueva_profesion
        print('Profesion cambiada con exito.')
    
    def set_centro_laboral(self, nuevo_centro_laboral):
        self.centro_laboral = nuevo_centro_laboral
        print('Centro laboral cambiado con exito.')
    
    def set_cursos(self, nuevos_cursos):
        self.cursos = nuevos_cursos
        print('Cursos cambiados con exito.')
    
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