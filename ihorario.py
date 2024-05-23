from abc import ABC, abstractmethod


class IHorario(ABC):
    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    
    def obtener_curso(self):
        return self.curso.obtener_nombre()
    
    def obtener_dia(self):
        return self.dia
    
    def obtener_hora_inicio(self):
        return self.hora_inicio
    
    def obtener_hora_fin(self):
        return self.hora_fin    
    
    @abstractmethod
    def obtener_datos(self):
        pass