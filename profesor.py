from usuario import Usuario


class Profesor(Usuario):
    def __init__(self, nombre, apellidos, correo, contrasena, profesion, centro_laboral):
        super().__init__(nombre, apellidos, correo, contrasena)
        self.profesesion = profesion
        self.centro_laboral = centro_laboral
        
    # Metodos
    