from horario import Horario
from fabrica_abstracta import FabricaAbstracta


class FabricaHorario(FabricaAbstracta):
    @staticmethod
    def crear_horario(curso, dia, hora_inicio, hora_fin):
        return Horario(curso, dia, hora_inicio, hora_fin)