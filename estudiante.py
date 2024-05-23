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
    
    def __repr__(self):
        return f'Estudiante({self.obtener_nombre()}, {self.obtener_apellidos()}, {self.obtener_correo()}, {self.obtener_contrasena()}, {self.obtener_ciclo()}, {self.obtener_carrera()}, {self.obtener_universidad()}, {self.obtener_codigo()}, {self.obtener_cursos()})'
    
    # GETTERS
    def obtener_datos(self):
        return {
            'nombre': self.obtener_nombre(),
            'apellidos': self.obtener_apellidos(),
            'correo': self.obtener_correo(),
            'ciclo': self.obtener_ciclo(),
            'carrera': self.obtener_carrera(),
            'universidad': self.obtener_universidad(),
            'codigo': self.obtener_codigo(),
            'cursos': self.obtener_cursos()
        }
    
    def obtener_ciclo(self):
        return self.ciclo
    
    def obtener_carrera(self):
        return self.carrera
    
    def obtener_universidad(self):
        return self.universidad
    
    def obtener_codigo(self):
        return self.codigo
    
    def obtener_calificaciones(self):
        return [f'[{calificacion.obtener_profesor()}: {calificacion.obtener_puntuacion()}]' for calificacion in self.calificaciones]
    
    # SETTERS    
    def modificar_datos(self, **kwargs):
        self.modificar_nombre(kwargs.get('nombre', self.obtener_nombre()))
        self.modificar_apellidos(kwargs.get('apellidos', self.obtener_apellidos()))
        self.modificar_correo(kwargs.get('correo', self.obtener_correo()))
        self.modificar_contrasena(kwargs.get('contrasena', self.obtener_contrasena()))
        self.ciclo = kwargs.get('ciclo', self.ciclo)
        self.carrera = kwargs.get('carrera', self.carrera)
        self.universidad = kwargs.get('universidad', self.universidad)
        self.codigo = kwargs.get('codigo', self.codigo)
    
    # CURSO
    def matricular_curso(self, curso):
        if curso in self._cursos:
            print(f'Estudiante {self.obtener_nombre()} ya esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.estudiantes.append(self)
            self._cursos.append(curso)
            print(f'Estudiante {self.obtener_nombre()} matriculado al curso "{curso.nombre}" con exito.')
    
    def retirar_curso(self, curso):
        if curso not in self._cursos:
            print(f'Estudiante {self.obtener_nombre()} no esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.estudiantes.remove(self)
            self._cursos.remove(curso)
            print(f'Estudiante {self.obtener_nombre()} retirado del curso "{curso.nombre}".')
    
    # PROFESOR
    def ver_profesores(self):
        lista_profesores = []
        for curso in self._cursos:
            if curso.profesor.obtener_nombre() not in lista_profesores:
                lista_profesores.append(curso.profesor.obtener_nombre())
        return lista_profesores
    
    def calificar_profesor(self, profesor, puntuacion):
        if not profesor.obtener_nombre() in self.ver_profesores():
            print(f'No estás matriculado en ningún curso del profesor {profesor.obtener_nombre()} para calificarlo.')
            return
        
        for calificacion in self.calificaciones:
            if calificacion.obtener_profesor() == profesor:
                print(f'Estudiante ya ha calificado al profesor {profesor.obtener_nombre()}.')
                return
        
        calificacion = Calificacion(self, profesor, puntuacion)
        self.calificaciones.append(calificacion)
        profesor.recibir_calificacion(calificacion.obtener_puntuacion())
        print(f'Profesor {profesor.obtener_nombre()} calificado con éxito.')
        return