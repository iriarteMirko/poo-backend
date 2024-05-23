from usuario import Usuario
from calificacion import Calificacion


class Estudiante(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, universidad, carrera, ciclo, codigo):
        super().__init__(nombre, apellidos, correo, contrasena)
        self._universidad = universidad
        self._carrera = carrera
        self._ciclo = ciclo
        self._codigo = codigo
        self._cursos_favoritos = []
        self._calificaciones = []
    
    def __repr__(self):
        return (f'Estudiante(nombre={self.get_nombre()}, apellidos={self.get_apellidos()}, correo={self.get_correo()}, contrasena={self.get_contrasena()}, universidad={self.get_universidad()}, carrera={self.get_carrera()}, ciclo={self.get_ciclo()}, codigo={self.get_codigo()}, cursos={[curso.get_nombre() for curso in self.get_cursos()]})')
    
    def get_universidad(self):
        return self._universidad
    
    def set_universidad(self, universidad):
        self._universidad = universidad
    
    def get_carrera(self):
        return self._carrera
    
    def set_carrera(self, carrera):
        self._carrera = carrera
    
    def get_ciclo(self):
        return self._ciclo
    
    def set_ciclo(self, ciclo):
        self._ciclo = ciclo
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        self._codigo = codigo
    
    def get_cursos_favoritos(self):
        return self._cursos_favoritos
    
    def get_calificaciones(self):
        return self._calificaciones
    
    def get_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'ciclo': self.get_ciclo(),
            'carrera': self.get_carrera(),
            'universidad': self.get_universidad(),
            'codigo': self.get_codigo(),
            'cursos': [curso.get_nombre() for curso in self.get_cursos()],
            'cursos_favoritos': [curso.get_nombre() for curso in self.get_cursos_favoritos()],
            'calificaciones': [f'[{calificacion.get_profesor().get_nombre()}:{calificacion.get_puntuacion()}]' for calificacion in self.get_calificaciones()]
        }
    
    def modificar_datos(self, **kwargs):
        self.set_nombre()(kwargs.get('nombre', self.get_nombre()))
        self.set_apellidos(kwargs.get('apellidos', self.get_apellidos()))
        self.set_correo(kwargs.get('correo', self.get_correo()))
        self.set_contrasena(kwargs.get('contrasena', self.get_contrasena()))
        self.set_ciclo(kwargs.get('ciclo', self.get_ciclo()))
        self.set_carrera(kwargs.get('carrera', self.get_carrera()))
        self.set_universidad(kwargs.get('universidad', self.get_universidad()))
        self.set_codigo(kwargs.get('codigo', self.get_codigo()))
    
    # CURSO
    def matricular_curso(self, curso):
        if curso in self.get_cursos():
            print(f'Estudiante {self.get_nombre()} ya esta matriculado en el curso "{curso.get_nombre()}".')
        else:
            curso.agregar_estudiante(self)
            self.agregar_curso(curso)
            print(f'Estudiante {self.get_nombre()} matriculado al curso "{curso.get_nombre()}" con exito.')
    
    def retirar_curso(self, curso):
        if curso not in self.get_cursos():
            print(f'Estudiante {self.get_nombre()} no esta matriculado en el curso "{curso.get_nombre()}".')
        else:
            curso.retirar_estudiante(self)
            self.quitar_curso(curso)
            print(f'Estudiante {self.get_nombre()} retirado del curso "{curso.get_nombre()}".')
    
    # FAVORITOS
    def agregar_curso_favorito(self, curso):
        if curso in self.get_cursos_favoritos():
            print(f'El curso "{curso.get_nombre()}" ya esta en favoritos.')
        else:
            self.get_cursos_favoritos().append(curso)
            print(f'Curso "{curso.get_nombre()}" agregado a favoritos.')
    
    def quitar_curso_favorito(self, curso):
        if curso not in self.get_cursos_favoritos():
            print(f'El curso "{curso.get_nombre()}" no esta en favoritos.')
        else:
            self.get_cursos_favoritos().remove(curso)
            print(f'Curso "{curso.get_nombre()}" eliminado de favoritos.')
    
    # PROFESOR
    def ver_profesores(self):
        lista_profesores = []
        for curso in self.get_cursos():
            if curso.get_profesor().get_nombre() not in lista_profesores:
                lista_profesores.append(curso.get_profesor().get_nombre())
        return lista_profesores
    
    def calificar_profesor(self, profesor, puntuacion):
        if not profesor.get_nombre() in self.ver_profesores():
            print(f'No estás matriculado en ningún curso del profesor {profesor.get_nombre()} para calificarlo.')
            return
        
        for calificacion in self.get_calificaciones():
            if calificacion.get_profesor() == profesor:
                print(f'Estudiante ya ha calificado al profesor {profesor.get_nombre()}.')
                return
        
        calificacion = Calificacion(self, profesor, puntuacion)
        self.get_calificaciones().append(calificacion)
        profesor.agregar_puntuacion(calificacion.get_puntuacion())
        print(f'Profesor {profesor.get_nombre()} calificado con éxito.')
        return
    
    def moficicar_calificacion(self, profesor, puntuacion):
        for calificacion in self.get_calificaciones():
            if calificacion.get_profesor() == profesor:
                calificacion.set_puntuacion(puntuacion)
                print(f'Calificacion modificada con éxito.')
                return
            else:
                print(f'No se puede modificar calificacion, el estudiante no ha calificado al profesor {profesor.get_nombre()}.')
    
    def eliminar_calificacion(self, profesor):
        for calificacion in self.get_calificaciones():
            if calificacion.get_profesor() == profesor:
                self.get_calificaciones().remove(calificacion)
                profesor.quitar_puntuacion(calificacion.get_puntuacion())
                print(f'Calificacion eliminada con éxito.')
                return
            else:
                print(f'No se puede eliminar calificacion, el estudiante no ha calificado al profesor {profesor.get_nombre()}.')