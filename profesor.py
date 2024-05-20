from usuario import Usuario


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.profesesion = profesion
        self.centro_laboral = centro_laboral
    
    # GETTERS
    def get_profesion(self):
        return self.profesesion
    
    def get_centro_laboral(self):
        return self.centro_laboral
    
    def get_datos(self):
        print(f'Nombre: {self.get_nombre()}')
        print(f'Apellidos: {self.get_apellidos()}')
        print(f'Correo: {self.get_correo()}')
        print(f'Contrasena: {self.get_contrasena()}')
        print(f'Profesion: {self.get_profesion()}')
        print(f'Centro laboral: {self.get_centro_laboral()}')
    
    # SETTERS
    def set_profesion(self, nueva_profesion):
        self.profesesion = nueva_profesion
        print('Profesion cambiada con exito.')
    
    def set_centro_laboral(self, nuevo_centro_laboral):
        self.centro_laboral = nuevo_centro_laboral
        print('Centro laboral cambiado con exito.')
    
    def set_datos(self):
        self.set_nombre(input('Nuevo nombre: '))
        self.set_apellidos(input('Nuevos apellidos: '))
        self.set_correo(input('Nuevo correo: '))
        self.set_contrasena(input('Nueva contrasena: '))
        self.set_profesion(input('Nueva profesion: '))
        self.set_centro_laboral(input('Nuevo centro laboral: '))
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'profesion': self.get_profesion(),
            'centro_laboral': self.get_centro_laboral()
        }
    
    # CURSO
    def crear_curso(self):
        pass
    
    def modificar_curso(self):
        pass
    
    def eliminar_curso(self):
        pass
    
    def publicar_curso(self):
        pass    
    
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