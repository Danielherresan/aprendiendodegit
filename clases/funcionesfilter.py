#Funciones filter
lista = [2,3,4,523,32,6,8,12]
listaPares =[]
for elemento in lista:
    if elemento % 2 == 0:
        listaPares.append(elemento)
print (listaPares)
par = lambda valor : valor % 2 == 0
listaParesFiltrada = list (filter(par,lista))
print(listaParesFiltrada)
mayores = lambda valor : valor >= 12
listaMayores = list (filter(mayores, lista))
print (listaMayores)