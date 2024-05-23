from icalificacion import ICalificacion


class Calificacion(ICalificacion):
    def __init__(self, estudiante:object, profesor:object, puntuacion:int):
        super().__init__(estudiante, profesor)
        self._puntuacion:int = puntuacion
    
    def __repr__(self):
        return (f'Calificacion(Estudiante={self.get_estudiante().get_nombre()}, Profesor={self.get_profesor().get_nombre()}, puntuacion={self.get_puntuacion()})')
    
    def get_puntuacion(self):
        return self._puntuacion
    
    def set_puntuacion(self, puntuacion:int):
        self._puntuacion:int = puntuacion
    
    def get_datos(self):
        return {
            'estudiante': self.get_estudiante().get_nombre(),
            'profesor': self.get_profesor().get_nombre(),
            'puntuacion': self.get_puntuacion()
        }