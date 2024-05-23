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
        return f'Estudiante({self.nombre}, {self.apellidos}, {self.correo}, {self.contrasena}, {self.ciclo}, {self.carrera}, {self.universidad}, {self.codigo}, {self.cursos})'
    
    # PROPIEDADES
    @property
    def ciclo(self):
        return self.ciclo
    
    @ciclo.setter
    def ciclo(self, ciclo):
        self.ciclo = ciclo
    
    @property
    def carrera(self):
        return self.carrera
    
    @carrera.setter
    def carrera(self, carrera):
        self.carrera = carrera
    
    @property
    def universidad(self):
        return self.universidad
    
    @universidad.setter
    def universidad(self, universidad):
        self.universidad = universidad
    
    @property
    def codigo(self):
        return self.codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.codigo = codigo
    
    @property
    def calificaciones(self):
        return [f'[{calificacion.profesor}: {calificacion.puntuacion}]' for calificacion in self.calificaciones]
    
    # METODOS
    def obtener_datos(self):
        return {
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'correo': self.correo,
            'ciclo': self.ciclo,
            'carrera': self.carrera,
            'universidad': self.universidad,
            'codigo': self.codigo,
            'cursos': self.cursos
        }
    
    def modificar_datos(self, **kwargs):
        self.nombre(kwargs.get('nombre', self.nombre))
        self.apellidos(kwargs.get('apellidos', self.apellidos))
        self.correo(kwargs.get('correo', self.correo))
        self.contrasena(kwargs.get('contrasena', self.contrasena))
        self.ciclo = kwargs.get('ciclo', self.ciclo)
        self.carrera = kwargs.get('carrera', self.carrera)
        self.universidad = kwargs.get('universidad', self.universidad)
        self.codigo = kwargs.get('codigo', self.codigo)
    
    # CURSO
    def matricular_curso(self, curso):
        if curso in self.cursos:
            print(f'Estudiante {self.nombre} ya esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.agregar_estudiante(self)
            self.agregar_curso(curso)
            print(f'Estudiante {self.nombre} matriculado al curso "{curso.nombre}" con exito.')
    
    def retirar_curso(self, curso):
        if curso not in self.cursos:
            print(f'Estudiante {self.nombre} no esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.eliminar_estudiante(self)
            self.eliminar_curso(curso)
            print(f'Estudiante {self.nombre} retirado del curso "{curso.nombre}".')
    
    # PROFESOR
    def ver_profesores(self):
        lista_profesores = []
        for curso in self.cursos:
            if curso.profesor.nombre not in lista_profesores:
                lista_profesores.append(curso.profesor.nombre)
        return lista_profesores
    
    def calificar_profesor(self, profesor, puntuacion):
        if not profesor.nombre in self.ver_profesores():
            print(f'No estás matriculado en ningún curso del profesor {profesor.nombre} para calificarlo.')
            return
        
        for calificacion in self.calificaciones:
            if calificacion.profesor == profesor:
                print(f'Estudiante ya ha calificado al profesor {profesor.nombre}.')
                return
        
        calificacion = Calificacion(self, profesor, puntuacion)
        self.calificaciones.append(calificacion)
        profesor.agregar_calificacion(calificacion.puntuacion)
        print(f'Profesor {profesor.nombre} calificado con éxito.')
        return