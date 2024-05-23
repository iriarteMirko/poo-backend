from icalificacion import ICalificacion


class Calificacion(ICalificacion):
    def __init__(self, estudiante, profesor, puntuacion):
        super().__init__(estudiante, profesor)
        self.puntuacion = puntuacion
    
    def __repr__(self):
        return (f'Calificacion({self.estudiante.nombre}, {self.profesor.nombre}, {self.puntuacion})')
    
    # PROPIEDADES
    @property
    def puntuacion(self):
        return self.puntuacion
    
    # METODOS
    def obtener_datos(self):
        return {
            'estudiante': self.estudiante.nombre,
            'profesor': self.profesor.nombre,
            'puntuacion': self.puntuacion
        }