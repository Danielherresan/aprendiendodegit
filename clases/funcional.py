def linedesign(cantidad):
    print ('#'*cantidad)
linedesign(3)
#funciones lambdas
#lambda entradas : accion
line = lambda cantidad =12: print ('#'*cantidad)
line()
line(2)

sumar = lambda valor1 = 0, valor2 =0 : valor1 + valor2
restar = lambda valor1 = 0, valor2 =0 : valor1 - valor2
multiplicar = lambda valor1 = 0, valor2 =0 : valor1 * valor2
dividir = lambda valor1 = 0, valor2 =0 : valor1 / valor2
resultadp = sumar (1,2)
print(resultadp)

calculadora = lambda accion, valor1=0, valor2=0 :print (accion(valor1, valor2))
calculadora (sumar,42,48)

#Funciones Map
line(35)
listaNumeros = [1,2,3,4,5,6]
potenciador = lambda base, exponente : base ** exponente 
print (potenciador (2,4))