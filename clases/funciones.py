#Funciones sin entrada
print ('#'*60)
print ("hola")
print ("como esta?")
print ('#'*60)
def lineDesign():
    print('#'*60)
lineDesign()
print ("hola")
print ("como esta?")
lineDesign()
# funciones con una entrada
def lineDesignC(cantidad=2):
    print ('#'*cantidad)
lineDesignC(12)
lineDesignC()
# funcion suma

def sumar (valor1=0, valor2=0):
    return valor1+ valor2
def restar (valor1=0, valor2=0):
    return valor1 - valor2
def multiplicar  (valor1=0, valor2=1):
    return valor1 * valor2
def dividir (valor1=0, valor2=1):
    return valor1 / valor2
print (sumar (2,2))
print (sumar ())
#funciones que utilizan otras
def calculadora (accion, valor1, valor2):
    print (accion(valor1, valor2))
lineDesignC(30)
calculadora (sumar, 1,1)
calculadora (dividir, 1,2)
calculadora (multiplicar, 73,77)
calculadora (restar, 73,77)

