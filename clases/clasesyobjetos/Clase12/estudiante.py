import persona as p
class Estudiante(p.Persona):
    def __init__ (self, nombreIn, edadIn, idIn, carreraIn, semestreIn):
        p.Persona.__init__(self,nombreIn,edadIn,idIn)
        self.carrera = carreraIn
        self.semestre = semestreIn
    
    def estudiar (self,materia) :
        print (f'hola soy {self.nombre} y estoy muy motivad@ pues estudiaré {materia}')