class TortaRedonda:
    def __init__ (self,saborIngresado):
        #Definiendo atributos
        self.forma = 'Redonda'
        self.sabor = saborIngresado
        #acción al crear objeto
        print ('Soy una torta nueva')
    def mostrar_atributos (self):
        print (f'soy de forma {self.forma} y de sabor {self.sabor}')


#Creó la torta
tortaChocolate = TortaRedonda('Chocolate')
tortaVainilla = TortaRedonda('Vainilla')
#Se muestra en pantalla los atributos
print (tortaChocolate.sabor)
print (tortaVainilla.sabor)
print (tortaChocolate.forma)
print (tortaVainilla.forma)

#
tortaChocolate.mostrar_atributos()
tortaVainilla.mostrar_atributos()
