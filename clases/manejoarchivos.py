#leer

archivo = open ('poema.txt', encoding  = 'UTF-8')
print (archivo)
lineas = archivo.readlines()
archivo.close()
print (lineas)
listaRenglones = []
with open ('poema.txt', encoding  = 'UTF-8') as lineas:
    for line in lineas :
        print (line)
        listaRenglones.append(line)

print (listaRenglones)

print ('Saludo:\nHola como estas')
print ('Saludo:\t\t\t\tHola como estas')

nombre  = input ('ingrese su nombre : ')
edad = int (input ('ingrese su edad : '))
opinion  = input ('ingrese su opinion : \n')

archivo = open ('opinion.txt','w', encoding='UTF-8')
archivo.write(f'Opinion de {nombre} \n')
archivo.write(f'Edad :  {edad} \n')
archivo.write(f'Reseña:\n  {opinion} \n')
archivo.close()


