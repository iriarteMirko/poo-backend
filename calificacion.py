from icalificacion import ICalificacion


class Calificacion(ICalificacion):
    def __init__(self, estudiante, profesor, puntuacion):
        self.estudiante = estudiante
        self.profesor = profesor
        self.puntuacion = puntuacion

    def get_datos(self):
        return {
            'estudiante': self.estudiante.get_nombre(),
            'profesor': self.profesor.get_nombre(),
            'puntuacion': self.puntuacion
        }

    def get_estudiante(self):
        return self.estudiante

    def get_profesor(self):
        return self.profesor

    def get_puntuacion(self):
        return self.puntuacion
