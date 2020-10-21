
import estudiante as es
class Egresado ( es.Estudiante):
    def __init__ (self,nombreIn, edadIn, idIn, carreraIn, fechaIn):
        es.Estudiante.__init__(self,nombreIn,edadIn,idIn, carreraIn,'Egresado')
        self.fecha = fechaIn
    def trabajar (self,empresa):
        print (f'Hola soy {self.nombre}, Voy a trabajar en la empresa {empresa}')