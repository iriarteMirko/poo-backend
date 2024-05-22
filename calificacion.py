class Calificacion:
    def __init__(self, estudiante, profesor, puntuacion):
        self.estudiante = estudiante
        self.profesor = profesor
        self.puntuacion = puntuacion
    
    def __repr__(self):
        return f'Calificacion({self.estudiante.obtener_nombre()}, {self.profesor.obtener_nombre()}, {self.puntuacion})'
    
    def obtener_datos(self):
        return {
            'estudiante': self.estudiante.obtener_nombre(),
            'profesor': self.profesor.obtener_nombre(),
            'puntuacion': self.puntuacion
        }
    
    def obtener_estudiante(self):
        return self.estudiante
    
    def obtener_profesor(self):
        return self.profesor
    
    def obtener_puntuacion(self):
        return self.puntuacion
