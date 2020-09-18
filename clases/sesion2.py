preguntaNombre = 'ingrese su nombre por favor : '
preguntaEdad = 'ingrese por favor su edad : '
preguntaEstatura = 'ingrese por favor su estatura : '
mensajeBienvenida = 'Bienvenido {} tu edad {} y tu estura {}'
ejemploTextoLargo  = """
        algo algo algo algo algo algo algo algo 
        como como como como como como como como  
"""
nombre = input(preguntaNombre)
edad = int(input(preguntaEdad))
estatura = float(input(preguntaEstatura))

print (type (edad))
print (type (estatura))
print ("hola como estas", nombre, "?")
print (f"hola como estas {nombre}? tu edad es de {edad} y tu estatura {estatura}")
print (mensajeBienvenida.format(nombre,edad, estatura))
print (ejemploTextoLargo)