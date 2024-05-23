from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena):
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        self._cursos = []
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def get_apellidos(self):
        return self._apellidos
    
    def set_apellidos(self, nuevos_apellidos):
        self._apellidos = nuevos_apellidos
    
    def get_correo(self):
        return self._correo
    
    def set_correo(self, nuevo_correo):
        self._correo = nuevo_correo
    
    def get_contrasena(self):
        return self._contrasena
    
    def set_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena
    
    def get_cursos(self):
        return self._cursos
    
    def iniciar_sesion(self, correo, contrasena):
        if correo == self.get_correo() and contrasena == self.get_contrasena():
            print('Sesion iniciada con exito.')
        else:
            print('Correo o contrasena incorrectos.')
    
    def recuperar_contrasena(self, correo):
        if correo == self.get_correo():
            print(f'La contrasena es: {self.get_contrasena()}')
        else:
            print('Correo incorrecto.')
    
    def agregar_curso(self, curso):
        self._cursos.append(curso)
    
    def quitar_curso(self, curso):
        self._cursos.remove(curso)
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def get_datos(self):
        pass
    
    @abstractmethod
    def modificar_datos(self):
        pass