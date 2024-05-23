from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena):
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasena = contrasena
        self._cursos = []
    
    # PROPIEDADES
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def apellidos(self):
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, nuevos_apellidos):
        self._apellidos = nuevos_apellidos
    
    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo
    
    @property
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena
    
    @property
    def cursos(self):
        return [curso.nombre for curso in self.cursos]
    
    # METODOS
    def iniciar_sesion(self, correo, contrasena):
        if correo == self.correo and contrasena == self.contrasena:
            print('Sesion iniciada con exito.')
        else:
            print('Correo o contrasena incorrectos.')
    
    def recuperar_contrasena(self, correo):
        if correo == self.correo:
            print(f'La contrasena es: {self.contrasena}')
        else:
            print('Correo incorrecto.')
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def eliminar_curso(self, curso):
        self.cursos.remove(curso)
    
    # METODOS ABSTRACTOS
    @abstractmethod
    def obtener_datos(self):
        pass
    
    @abstractmethod
    def modificar_datos(self):
        pass