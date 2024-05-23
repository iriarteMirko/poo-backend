from ihorario import IHorario


class Horario(IHorario):
    def __init__(self, curso, dia, hora_inicio, hora_fin):
        super().__init__(curso, dia, hora_inicio, hora_fin)
    
    def __repr__(self):
        return f'Horario({self.obtener_curso()}, {self.obtener_diayhora()})'
    
    def obtener_datos(self):
        return {
            'curso': self.obtener_curso(),
            'dia': self.obtener_dia(),
            'hora_inicio': self.obtener_hora_inicio(),
            'hora_fin': self.obtener_hora_fin()
        }
    
    def obtener_diayhora(self):
        return f'{self.obtener_dia()} de {self.obtener_hora_inicio()} a {self.obtener_hora_fin()}'