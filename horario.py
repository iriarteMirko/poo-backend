from ihorario import IHorario


class Horario(IHorario):
    def __init__(self, curso:object, dia:str, hora_inicio:str, hora_fin:str):
        super().__init__(curso)
        self._dia:str = dia
        self._hora_inicio:str = hora_inicio
        self._hora_fin:str = hora_fin
    
    def __repr__(self):
        return (f'Horario(Curso={self.get_curso()}, dia={self.get_dia()}, hora_inicio={self.get_hora_inicio()}, hora_fin={self.get_hora_fin()})')
    
    def get_datos(self):
        return {
            'curso': self.get_curso(),
            'dia': self.get_dia(),
            'hora_inicio': self.get_hora_inicio(),
            'hora_fin': self.get_hora_fin()
        }
    
    def get_dia(self):
        return self._dia
    
    def set_dia(self, dia:str):
        self._dia:str = dia
    
    def get_hora_inicio(self):
        return self._hora_inicio
    
    def set_hora_inicio(self, hora_inicio:str):
        self._hora_inicio:str = hora_inicio
    
    def get_hora_fin(self):
        return self._hora_fin
    
    def set_hora_fin(self, hora_fin:str):
        self._hora_fin:str = hora_fin