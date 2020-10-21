class Person ():
    def __init__ (self,edadIn, estaturaIn, idIn, nombreIn, sexoIn):
        print ("Hola estoy vivo")
        self.estatura = estaturaIn
        self.edad = edadIn
        self.id = idIn
        self.nombre =nombreIn
        self.sexo = sexoIn
        self.raza = 'Humana'
    def hablar (self, mensaje):
        print (f'hola soy {self.nombre} y tengo un mensaje : \n {mensaje}')
    
    def siglo (self):
        return 100-self.edad

class Doctor (Person):

    def __init__(self,edadIn, estaturaIn, idIn, nombreIn, sexoIn,espIn):
        Person.__init__(self,edadIn,estaturaIn,idIn,nombreIn,sexoIn)
        self.especialidad = espIn

    def recetar_formula (self, enfermedad):
        print (f'Para la enfermedad {enfermedad} recomiendo que sigas las instrucciones')

class Estudent (Person):
    def __init__ (self,edadIn, estaturaIn, idIn, nombreIn, sexoIn,carreraIn,semestreIn):
        Person.__init__(self,edadIn,estaturaIn,idIn,nombreIn,sexoIn)
        self.carrera = carreraIn
        self.semestre = semestreIn
    
    def estudiar (self, materia):
        print (f'Se procede a estudiar la materia {materia}')
    def calcular_faltante (self,largoCarrera):
        return largoCarrera-self.semestre


persona = Person(25,1.76,3213246,'Pepito','Hombre')
print (persona.estatura)
persona.hablar('Espero que todos anden muy bien!!')
faltante = persona.siglo()
print (f'me faltan {faltante} para cumplir mi primer siglo')
doctora = Doctor(27, 1.67,128739,'Nataly','Mujer', 'Neumología')
print(doctora.siglo())
doctora.hablar("Soy tu doctora")
doctora.recetar_formula('gripe')
estudiante = Estudent (18,1.78,132789,'Albert','Hombre','Nanotecnología',6)
estudiante.hablar('Estoy a finales de semestre')
estudiante.siglo()
estudiante.estudiar('Física de particulas')
restante = estudiante.calcular_faltante(10)
print (f'Al estudiante {estudiante.nombre} le falta {restante} semestres para terminar la carrera')