class Persona:
    def __init__ (self, estaturaIngresado, 
    pesoIngresado,nombreIngresado, 
    idIngresado, edadIngresado):
        self.raza = 'Humana'
        self.estatura = estaturaIngresado
        self.edad = edadIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.id = idIngresado
        print ('Hola mundo estoy viv@')
    def caminar (self):
        print ("hola voy a caminar")
    def saludo (self, saludoEspecial):
        print (saludoEspecial)

class Colombiano():
    def __init__(self, departamento, ciudad):
        self.departamento = departamento
        self.ciudad = ciudad
        self.pais = 'Colombia'
class Arquitecto (Persona):
    
    def dibujar_Planos (self):
        print (f'Hola soy {self.nombre} voy a dibujar el plano')
class Biomedico (Persona, Colombiano):
    def __init__(self, 
                estaturaIngresado, 
                pesoIngresado,
                nombreIngresado, 
                idIngresado, 
                edadIngresado,
                departamento,
                ciudad,
                universidad):
        Persona.__init__(self, 
                        estaturaIngresado, 
                        pesoIngresado,
                        nombreIngresado, 
                        idIngresado, 
                        edadIngresado)
        Colombiano.__init__(self,departamento,ciudad)
        self.universidad = universidad
        
    def cultivar_celulas (self):
        print (f'Hola soy {self.nombre} voy a cultivar celulas')

karla = Arquitecto(1.62,48,'Karla',1032321323,18)
karla.caminar()
juan = Biomedico (1.76,82,'Juan Pablo',912837981237,23,'Antioquia','Medellín','Universidad CES')
juan.caminar()
karla.saludo('HOLI CRAYOLI')
juan.saludo('HOLA COCACOLA')
karla.dibujar_Planos()
juan.cultivar_celulas()
print (juan.universidad)
print(juan.departamento)
print (juan.pais)