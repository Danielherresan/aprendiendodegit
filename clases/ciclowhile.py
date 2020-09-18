preguntarEstaDeAcuerdo = """
        si - Te vuelvo a saludar?
        no - me despido
""" 
preguntarNombre = "Por favor ingresa tu nombre : "

nombre = input(preguntarNombre)
print (f"Hola {nombre} te saludo espero que estes muy bien")
decision = input(preguntarEstaDeAcuerdo)
mensajeSaludo = f"Hola {nombre} te saludo nuevamente"
mensajeDespedida = f"chao {nombre} espero verte de nuevo"

while (decision == 'si'):
    print(mensajeSaludo)
    decision = input(preguntarEstaDeAcuerdo)
print (mensajeDespedida)

numeroSecreto = 9
preguntarNumero = 'Por favor ingrese un numero entero entre el 1 y el 10 : '
numeroEscogido = int (input(preguntarNumero))
mensajeDerrota = 'No ese el número !! sigue intentando'
mensajeVictoria = 'Bien!! acertaste el número!!'
while (numeroEscogido != numeroSecreto):
    print (mensajeDerrota)
    numeroEscogido = int (input(preguntarNumero))
print(mensajeVictoria)


