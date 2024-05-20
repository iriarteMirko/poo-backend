from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.ciclo = ciclo
        self.carrera = carrera
        self.universidad = universidad
        self.codigo = codigo
    
    # GETTERS
    def get_ciclo(self):
        return self.ciclo
    
    def get_carrera(self):
        return self.carrera
    
    def get_universidad(self):
        return self.universidad
    
    def get_codigo(self):
        return self.codigo
    
    def get_datos(self):
        print(f'ESTUDIANTE: {self.get_nombre()} {self.get_apellidos()}')
        print(f' - Correo: {self.get_correo()}')
        print(f' - Contrasena: {self.get_contrasena()}')
        print(f' - Ciclo: {self.get_ciclo()}')
        print(f' - Carrera: {self.get_carrera()}')
        print(f' - Universidad: {self.get_universidad()}')
        print(f' - Codigo: {self.get_codigo()}')
        print(f' - Cursos: {self.get_cursos()}')
        print('\n')
    
    # SETTERS
    def set_ciclo(self, nuevo_ciclo):
        self.ciclo = nuevo_ciclo
    
    def set_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
    
    def set_universidad(self, nueva_universidad):
        self.universidad = nueva_universidad
        
    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo
    
    def set_datos(self):
        pass
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'ciclo': self.get_ciclo(),
            'carrera': self.get_carrera(),
            'universidad': self.get_universidad(),
            'codigo': self.get_codigo(),
            'cursos': self.get_cursos()
        }
    
    def registrarse(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_correo(correo)
        self.set_contrasena(contrasena)
        self.set_ciclo(ciclo)
        self.set_carrera(carrera)
        self.set_universidad(universidad)
        self.set_codigo(codigo)
    
    # CURSO
    def matricular_curso(self, curso):
        curso.agregar_estudiante(self)
        self.cursos.append(curso.nombre)
        print(f'Estudiante {self.get_nombre()} matriculado al curso "{curso.nombre}" con exito.')
        print('\n')
    
    def retirar_curso(self, curso):
        curso.eliminar_estudiante(self)
        self.cursos.remove(curso)
        print(f'Estudiante {self.get_nombre()} retirado del curso "{curso.nombre}".')
        print('\n')
    
    def ver_profesores(self):
        for curso in self.cursos:
            print(f'Profesor: {curso.get_profesor()}')
            print('\n')
    
    def ver_horarios(self):
        pass