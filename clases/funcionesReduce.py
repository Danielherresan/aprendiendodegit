from functools import reduce
lista = [1,2,3,4,5]
acumulador = 0
for i in range (len (lista)) :
    acumulador += lista [i]
print (acumulador )
sumador  = lambda acumulador = 0, elemento = 0 : acumulador + elemento
resultado = reduce (sumador, lista)
print (resultado)
palabras = ['hola','como', 'estan','?']
union = lambda frase, palabra : frase +' '+ palabra
resultado = reduce (union, palabras)
print (resultado)