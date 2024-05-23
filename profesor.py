from usuario import Usuario
from fabrica_curso import FabricaCurso
from fabrica_horario import FabricaHorario


class Profesor(Usuario):
    def __init__(self, nombre:str, apellidos:str, correo:str, contrasena:str, profesion:str, centro_laboral:str):
        super().__init__(nombre, apellidos, correo, contrasena)
        self._profesion:str = profesion
        self._centro_laboral:str = centro_laboral
        self._puntuaciones:list = []
    
    def __repr__(self):
        return (f'Profesor(nombre={self.get_nombre()}, apellidos={self.get_apellidos()}, correo={self.get_correo()}, contrasena={self.get_contrasena()}, profesion={self.get_profesion()}, centro_laboral={self.get_centro_laboral()}, cursos={[curso.get_nombre() for curso in self.get_cursos()]}, puntuacion={self.get_puntuacion()})')
    
    def get_profesion(self):
        return self._profesion
    
    def set_profesion(self, profesion:str):
        self._profesion:str = profesion
    
    def get_centro_laboral(self):
        return self._centro_laboral
    
    def set_centro_laboral(self, centro_laboral:str):
        self._centro_laboral:str = centro_laboral
    
    def get_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'profesion': self.get_profesion(),
            'centro_laboral': self.get_centro_laboral(),
            'cursos': [curso.get_nombre() for curso in self.get_cursos()],
            'puntuacion': self.get_puntuacion()
        }
    
    def modificar_datos(self, **kwargs):
        self.set_nombre(kwargs.get('nombre', self.get_nombre()))
        self.set_apellidos(kwargs.get('apellidos', self.get_apellidos()))
        self.set_correo(kwargs.get('correo', self.get_correo()))
        self.set_contrasena(kwargs.get('contrasena', self.get_contrasena()))
        self.set_profesion(kwargs.get('profesion', self.get_profesion()))
        self.set_centro_laboral(kwargs.get('centro_laboral', self.get_centro_laboral()))
    
    # CURSO
    def crear_curso(self, nombre:str, descripcion:str):
        if any(curso.get_nombre() == nombre for curso in self.get_cursos()):
            print(f'Error: Ya existe un curso con el nombre "{nombre}".')
            return None
        
        factory = FabricaCurso()
        curso = factory.crear_curso(nombre, descripcion, self)
        self.agregar_curso(curso)
        print(f'Curso {curso.get_nombre()} creado con exito.')
        return curso
    
    def modificar_curso(self, curso:object, nombre=None or str, descripcion=None or str):
        if curso in self.get_cursos():
            if nombre:
                curso.set_nombre(nombre)
            if descripcion:
                curso.set_descripcion(descripcion)
            print(f'Curso modificado con éxito.')
        else:
            print(f'No se puede modificar curso, el profesor no esta asignado al curso {curso.get_nombre()}.')
    
    def eliminar_curso(self, curso:object):
        if curso in self.get_cursos():
            self.quitar_curso(curso)
            for estudiante in curso.get_estudiantes():
                estudiante.retirar_curso(curso)
            print(f'Curso "{curso.get_nombre()}" eliminado con éxito.')
        else:
            print(f'No se puede eliminar curso, el profesor no esta asignado al curso {curso.get_nombre()}.')
    
    # ESTUDIANTES
    def ver_estudiantes(self):
        lista_estudiantes = []
        for curso in self.get_cursos():
            for estudiante in curso.get_estudiantes():
                lista_estudiantes.append(estudiante.get_nombre() + '(' + curso.get_nombre() + ')')
        return lista_estudiantes
    
    # HORARIO
    def crear_horario(self, curso:object, dia:str, hora_inicio:str, hora_fin:str):
        if curso in self.get_cursos():
            factory = FabricaHorario()
            horario = factory.crear_horario(curso, dia, hora_inicio, hora_fin)
            curso.agregar_horario(horario)
            print(f'Horario creado con exito.')
            return horario
        else:
            print(f'No se puede crear horario, el profesor no esta asignado al curso {curso.get_nombre()}.')
            return None
    
    def modificar_horario(self, curso:object, horario:object, dia=None or str, hora_inicio=None or str, hora_fin=None or str):
        if curso in self.get_cursos():
            if horario in curso.get_horarios():
                if dia:
                    horario.set_dia(dia)
                if hora_inicio:
                    horario.set_hora_inicio(hora_inicio)
                if hora_fin:
                    horario.set_hora_fin(hora_fin)
                print('Horario modificado con exito.')
            else:
                print(f'No se puede modificar horario, el horario no pertenece al curso {curso.get_nombre()}.')
        else:
            print(f'No se puede modificar horario, el profesor no esta asignado al curso {curso.get_nombre()}.')
    
    def eliminar_horario(self, curso:object, horario:object):
        if curso in self.get_cursos():
            if horario in curso.get_horarios():
                curso.eliminar_horario(horario)
                print('Horario eliminado con exito.')
            else:
                print(f'No se puede eliminar horario, el horario no pertenece al curso {curso.get_nombre()}.')
        else:
            print(f'No se puede eliminar horario, el profesor no esta asignado al curso {curso.get_nombre()}.')
    
    # CALIFICACION
    def agregar_puntuacion(self, puntuacion:int):
        self._puntuaciones.append(puntuacion)
    
    def get_puntuacion(self):
        if self._puntuaciones:
            return round(sum(self._puntuaciones) / len(self._puntuaciones),1)
        return 0
    
    def quitar_puntuacion(self, puntuacion:int):
        self._puntuaciones.remove(puntuacion)
    
    def modificar_puntuacion(self, puntuacion:int, nueva_puntuacion:int):
        if puntuacion in self._puntuaciones:
            self._puntuaciones.remove(puntuacion)
            self._puntuaciones.append(nueva_puntuacion)
            print(f'Puntuacion modificada con éxito.')
        else:
            print(f'No se puede modificar puntuacion, la puntuacion no existe.')