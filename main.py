from usuario import Usuario
from profesor import Profesor
from estudiante import Estudiante
from curso import CursoFactory


estudiante1 = Estudiante('Juan', 'Perez', 'a@a', '123', '1', 'Ing. de Sistemas', 'UNI', '001')
estudiante2 = Estudiante('Maria', 'Gomez', 'c@c', '789', '2', 'Ing. de Sistemas', 'UNI', '002')
estudiante1.get_datos()
estudiante2.get_datos()


profesor1 = Profesor('Pedro', 'Garcia', 'b@b', '456', 'Ing. de Sistemas', 'UNI')
profesor1.get_datos()


fabrica = CursoFactory()
curso1 = fabrica.crear_curso('Curso 1', 'Descripcion 1', profesor1)
curso1.get_datos()

curso2 = fabrica.crear_curso('Curso 2', 'Descripcion 2', profesor1)
curso2.get_datos()

estudiante1.matricular_curso(curso1)
estudiante2.matricular_curso(curso1)
estudiante1.matricular_curso(curso2)
print(estudiante1.get_cursos())
print(estudiante2.get_cursos())
print('\n')

profesor1.get_cursos()

curso1.get_datos()
curso2.get_datos()

print(curso1.get_estudiantes())
print(curso2.get_estudiantes())
print('\n')

curso1.get_profesor()
curso2.get_profesor()