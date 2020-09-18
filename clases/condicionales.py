print (2 == 2)
print (2 != 2 )
print (2 >3)
print (2 <3)
print (2 == 2 and 2 != 2  )
print (2 == 2 and 3 != 2  )
print (2 == 2 or 2 != 2  )
print (2 != 2 or 3 != 2  )
print (2 != 2 or 3 != 3  )
preguntaEdad = 'Ingrese su edad : '
mensajeMayorEdad = 'Puedes pasar eres mayor'
mensajeMayorEdadBienvenido = 'Bienvenido a nuestro bar'
mensajeMenorEdad = 'Eres menor de edad no puedes ingresar a nuestro bar'
mensajeDescuento = 'Eres afortunado tienes un 40% de de descuento el día de hoy'
mensajeDescuentoAdultoMayor = 'Eres afortunado tienes un 50% de de descuento el día de hoy'
edad = int (input(preguntaEdad))
if (edad >= 18 and edad <40 ):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)a
elif (edad >= 40 and edad <=50 ):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)
    print (mensajeDescuento)
elif (edad > 50 ):
    print (mensajeMayorEdad)
    print (mensajeMayorEdadBienvenido)
    print (mensajeDescuentoAdultoMayor)
else :
    print (mensajeMenorEdad)
print ("CHAOO!!")
