from ihorario import IHorario


class Horario(IHorario):
    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    
    def get_datos(self):
        return {
            'curso': self.curso.nombre,
            'dia': self.dia,
            'hora_inicio': self.hora_inicio,
            'hora_fin': self.hora_fin
        }
    
    def modificar_horario(self, dia=None, hora_inicio=None, hora_fin=None):
        if dia:
            self.dia = dia
        if hora_inicio:
            self.hora_inicio = hora_inicio
        if hora_fin:
            self.hora_fin = hora_fin
        print('Horario modificado con éxito.')