from fabrica_abstracta import FabricaHorariosAbstracta
from horario import Horario


class FabricaHorario(FabricaHorariosAbstracta):
    @staticmethod
    def crear_horario(curso:object, dia:str, hora_inicio:str, hora_fin:str):
        return Horario(curso, dia, hora_inicio, hora_fin)