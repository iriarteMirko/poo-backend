from horario import Horario


class HorarioFactory:
    @staticmethod
    def crear_horario(curso, dia, hora_inicio, hora_fin):
        return Horario(curso, dia, hora_inicio, hora_fin)