class Persona:
    def __init__(self, nombre='', apellido='', edad=0, dni=0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni = dni 

    def __str__(self):
        return "Nombre: " + self.__nombre +"\nApellido: " + self.__apellido + "\nEdad: "+ str(self.__edad) + "\nDNI: " + str(self.__dni)

    def mayorEdad(self):
        return self._edad >= 18


#### PROGRAMA PRINCIPAL   ####