from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellidos, correo, contrasena, cursos=[]):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__contrasena = contrasena
        self.__cursos = cursos
    
    # GETTERS       
    def get_nombre(self):
        return self.__nombre
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_correo(self):
        return self.__correo
    
    def get_contrasena(self):
        return self.__contrasena
    
    def get_cursos(self):
        return self.__cursos
    
    def get_datos(self):
        print(f'Nombre: {self.get_nombre()}')
        print(f'Apellidos: {self.get_apellidos()}')
        print(f'Correo: {self.get_correo()}')
        print(f'Contrasena: {self.get_contrasena()}')
        print(f'Cursos: {self.get_cursos()}')
    
    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        print('Nombre cambiado con exito.')
    
    def set_apellidos(self, nuevos_apellidos):
        self.__apellidos = nuevos_apellidos
        print('Apellidos cambiados con exito.')
    
    def set_correo(self, nuevo_correo):
        self.__correo = nuevo_correo
        print('Correo cambiado con exito.')
    
    def set_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        print('Contrasena cambiada con exito.')
    
    def set_cursos(self, nuevos_cursos):
        self.__cursos = nuevos_cursos
        print('Cursos cambiados con exito.')
    
    def set_datos(self):
        pass
    
    # METODOS
    def enviar_datos(self):
        return {
            'nombre': self.get_nombre(),
            'apellidos': self.get_apellidos(),
            'correo': self.get_correo(),
            'cursos': self.get_cursos()
        }
    
    def registrarse(self):
        pass
    
    def iniciar_sesion(self):
        pass
    
    def recuperar_contrasena(self):
        pass

u = Usuario('Juan', 'Perez', 'a@a', '123',)

u.get_datos()
print(u.enviar_datos())
u.set_datos()