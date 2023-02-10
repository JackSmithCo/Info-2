class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

#Setters
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    def asignarCedula(self, cedula):
        self.__cedula=cedula
    def asignarGenero(self, genero):
        self.__genero=genero

#Getters
    def verNombre(self):
        return self.__nombre
    
    def verCedula(self):
        return self.__cedula
        
    def verGenero(self):
        return self.__genero

class Paciente(Persona):
    def __init__(self):
        self.__servicio = ""
    def asignarServicio(self, servicio):
        self.__servicio=servicio
    def verServicio(self, servicio):
        return self.__servicio

class Empleado_Hospital(Persona):
    def __init__(self):
        self.__turno= ""
    def asignarTruno(self, turno):
        self.__turno=turno
    def verTurno(self, turno):
        return self.__turno

class Enfermera(Empleado_Hospital):
    def __init__(self):
        self.__rango = ""
    def asignarRango(self, rango):
        self.__rango = rango
    def verRango(self, rango):
        return self.__rango


p1 = Paciente()
p2 = Paciente()
p1.asignarNombre("Aurelio Cheveroni")
p1.asignarCedula("1128429190")
p1.asignarGenero("No definido por la naturaleza")
print(p1,verNombre())

