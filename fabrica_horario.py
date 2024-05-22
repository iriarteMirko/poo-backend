from fabrica_abstracta import FabricaHorariosAbstracta
from horario import Horario


class FabricaHorario(FabricaHorariosAbstracta):
    @staticmethod
    def crear_horario(curso, dia, hora_inicio, hora_fin):
        return Horario(curso, dia, hora_inicio, hora_fin)