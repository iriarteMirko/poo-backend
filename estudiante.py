from usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, ciclo, carrera, universidad, codigo):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.ciclo = ciclo
        self.carrera = carrera
        self.universidad = universidad
        self.codigo = codigo
        self.cursos = []
    
    # GETTERS
    def get_ciclo(self):
        return self.ciclo
    
    def get_carrera(self):
        return self.carrera
    
    def get_universidad(self):
        return self.universidad
    
    def get_codigo(self):
        return self.codigo
    
    def get_cursos(self):
        return self.cursos
    
    def get_datos(self):
        print(f'Nombre: {self.get_nombre()}')
        print(f'Apellidos: {self.get_apellidos()}')
        print(f'Correo: {self.get_correo()}')
        print(f'Contrasena: {self.get_contrasena()}')
        print(f'Ciclo: {self.get_ciclo()}')
        print(f'Carrera: {self.get_carrera()}')
        print(f'Universidad: {self.get_universidad()}')
        print(f'Codigo: {self.get_codigo()}')
    
    # SETTERS
    def set_ciclo(self, nuevo_ciclo):
        self.ciclo = nuevo_ciclo
        print('Ciclo cambiado con exito.')
    
    def set_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
        print('Carrera cambiada con exito.')
    
    def set_universidad(self, nueva_universidad):
        self.universidad = nueva_universidad
        print('Universidad cambiada con exito.')
        
    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo
        print('Codigo cambiado con exito.')
    
    def set_cursos(self, nuevos_cursos):
        return super().set_cursos(nuevos_cursos)
    
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
            'codigo': self.get_codigo()
        }
    
    def matricular_curso(self):
        pass
    
    def ver_cursos(self):
        pass
    
    def ver_profesores(self):
        pass
    
    def ver_horarios(self):
        pass