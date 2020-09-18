#Funciones map
numerosListas = [1,2,3,4,5]
numerosListasCuadrado = []
for elemento in numerosListas :
    numerosListasCuadrado.append(elemento**2)
print (numerosListasCuadrado)
cuadrado = lambda base : base **2
listaCuadrados = list (map(cuadrado,numerosListas))
restarDos = lambda numero : numero -2
listaRestada = list (map(restarDos,numerosListas))
print (listaCuadrados)
print (listaRestada)