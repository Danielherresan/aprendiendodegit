class Persona():
    #Creación
    def __init__ (self, nombreIn, edadIn,idIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
    #Acciones
    #Hablar
    def hablar (self, mensaje) :
        print (f'Hola soy {self.nombre} y tengo algo que decir : {mensaje}')
    #Comer
    def comer (self, plato):
        print (f'Hola soy {self.nombre} y voy a comer un delicioso {plato}')
