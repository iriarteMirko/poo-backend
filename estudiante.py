from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.ciclo = ciclo
        self.carrera = carrera
        self.universidad = universidad
        self.codigo = codigo
    
    # GETTERS
    def get_datos(self):
        print(f'ESTUDIANTE: {self.get_nombre()} {self.get_apellidos()}')
        print(f' - Correo: {self.get_correo()}')
        print(f' - Contrasena: {self.get_contrasena()}')
        print(f' - Ciclo: {self.ciclo}')
        print(f' - Carrera: {self.carrera}')
        print(f' - Universidad: {self.universidad}')
        print(f' - Codigo: {self.codigo}')
        print(f' - Cursos: {self.cursos}')
    
    # SETTERS    
    def set_datos(self, nuevo_nombre, nuevos_apellidos, nuevo_correo, nueva_contrasena, nuevo_ciclo, nueva_carrera, nueva_universidad, nuevo_codigo):
        self.set_nombre(nuevo_nombre)
        self.set_apellidos(nuevos_apellidos)
        self.set_correo(nuevo_correo)
        self.set_contrasena(nueva_contrasena)
        self.ciclo = nuevo_ciclo
        self.carrera = nueva_carrera
        self.universidad = nueva_universidad
        self.codigo = nuevo_codigo
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'ciclo': self.ciclo,
            'carrera': self.carrera,
            'universidad': self.universidad,
            'codigo': self.codigo,
            'cursos': self.cursos
        }
    
    def registrarse(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_correo(correo)
        self.set_contrasena(contrasena)
        self.ciclo = ciclo
        self.carrera = carrera
        self.universidad = universidad
        self.codigo = codigo
    
    # CURSO
    def matricular_curso(self, curso):
        if curso.nombre in self.cursos:
            print(f'Estudiante {self.get_nombre()} ya esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.agregar_estudiante(self)
            self.cursos.append(curso)
            print(f'Estudiante {self.get_nombre()} matriculado al curso "{curso.nombre}" con exito.')
        
    def retirar_curso(self, curso):
        if curso.nombre not in self.cursos:
            print(f'Estudiante {self.get_nombre()} no esta matriculado en el curso "{curso.nombre}".')
        else:
            curso.eliminar_estudiante(self)
            self.cursos.remove(curso)
            print(f'Estudiante {self.get_nombre()} retirado del curso "{curso.nombre}".')
    
    # PROFESOR
    def ver_profesores(self):
        lista_profesores = []
        for curso in self.cursos:
            if curso.profesor not in lista_profesores:
                lista_profesores.append(curso.profesor)
    
    # HORARIO
    def ver_horarios(self):
        pass