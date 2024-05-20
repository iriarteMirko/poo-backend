class Curso:
    def __init__(self, nombre, descripcion, profesor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesor = profesor
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)
    
    def get_estudiantes(self):
        lista_estudiantes = []
        for estudiante in self.estudiantes:
            lista_estudiantes.append(estudiante.get_nombre())
        if lista_estudiantes:
            print(lista_estudiantes)
        else:
            return []
    
    def get_profesor(self):
        print(self.profesor.get_nombre() + ' ' + self.profesor.get_apellidos())
    
    def get_datos(self):
        print(f'CURSO: {self.nombre}')
        print(f' - Descripcion: {self.descripcion}')
        print(f' - Profesor: {self.get_profesor()}')
        print(f' - Estudiantes: {self.get_estudiantes()}')
