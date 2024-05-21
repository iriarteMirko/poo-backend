from usuario import Usuario
from calificacion import Calificacion


class Estudiante(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.ciclo = ciclo
        self.carrera = carrera
        self.universidad = universidad
        self.codigo = codigo
        self.calificaciones = []
    
    # GETTERS
    def get_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'ciclo': self.ciclo,
            'carrera': self.carrera,
            'universidad': self.universidad,
            'codigo': self.codigo,
            'cursos': self.get_cursos()
        }
    
    # SETTERS    
    def set_datos(self, **kwargs):
        self.set_nombre(kwargs.get('nombre', self.get_nombre()))
        self.set_apellidos(kwargs.get('apellidos', self.get_apellidos()))
        self.set_correo(kwargs.get('correo', self.get_correo()))
        self.set_contrasena(kwargs.get('contrasena', self.get_contrasena()))
        self.ciclo = kwargs.get('ciclo', self.ciclo)
        self.carrera = kwargs.get('carrera', self.carrera)
        self.universidad = kwargs.get('universidad', self.universidad)
        self.codigo = kwargs.get('codigo', self.codigo)
    
    # CURSO
    def matricular_curso(self, curso):
        if curso in self._cursos:
            print(f'Estudiante {self.get_nombre()} ya esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.estudiantes.append(self)
            self._cursos.append(curso)
            print(f'Estudiante {self.get_nombre()} matriculado al curso "{curso.nombre}" con exito.')
    
    def retirar_curso(self, curso):
        if curso not in self._cursos:
            print(f'Estudiante {self.get_nombre()} no esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.estudiantes.remove(self)
            self._cursos.remove(curso)
            print(f'Estudiante {self.get_nombre()} retirado del curso "{curso.nombre}".')
    
    # PROFESOR
    def ver_profesores(self):
        lista_profesores = []
        for curso in self._cursos:
            if curso.profesor.get_nombre() not in lista_profesores:
                lista_profesores.append(curso.profesor.get_nombre())
        return lista_profesores
    
    def calificar_profesor(self, profesor, puntuacion):
        for calificacion in self.calificaciones:
            if calificacion.get_profesor() == profesor:
                return f'Estudiante {self.get_nombre()} ya ha calificado al profesor {profesor.get_nombre()}.'
        
        calificacion = Calificacion(self, profesor, puntuacion)
        self.calificaciones.append(calificacion)
        profesor.recibir_calificacion(calificacion)
        return f'Profesor {profesor.get_nombre()} calificado con éxito.'