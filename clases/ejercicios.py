#Datos inciales
listaDolares = [20000,30000,4000,2500,1000,7600]

#Preguntas
preguntaMenu = '''
Por favor ingrese alguna de estas opciones:
            1- Convertir dolares 
            2- Mostrar categoria de ingresos
            3- Ver máximo, minimo y promedio de ingresos 
            4- Para salir del programa
: '''
preguntaConversionDolares = '''
Por favor ingrese alguna de estas opciones:
            C- Convertir a pesos colombianos
            D- Convertir a dolares
            E- Convertir a euros
: '''

#---Mensajes Error---# 
mensajeErrorNumero = 'Recuerde ingresar una opción válida 1,2,3,4'
mensajeErrorMoneda = 'Recuerde ingresar una opción válida C,D,E'
#---Mensajes Informativos---# 
mensajeOpcion = 'Usted escogio la opción {}'
mensajeSalida = 'Gracias por usar el programa'
mensajeDolares = 'No es necesaria la conversión, pero se muestra la lista'



#Incio código
opcion = int (input(preguntaMenu))
#Calculos preliminares
listaPesos= []
listaEuros = []
listaClasificacion = []
# ---Pasando a pesos 1 dolar = COP 3700---#
for elemento in listaDolares:
    pesos  = elemento * 3700
    listaPesos.append(pesos)
# ---Pasando a 1Euro =(1Dolar*.84)---#
for elemento in listaDolares:
    euros  = (elemento*0.84) 
    listaEuros.append(euros)
# ---Detectando los estados de salud---#
for elemento in listaDolares:
    clasificacion = ''
    if (elemento < 1000 ):
        clasificacion = 'Ingresos bajos'
    elif (elemento >= 1000 and elemento < 7000):
        clasificacion = 'Ingresos medios'
    elif (elemento >= 7000 and elemento < 20000):
        clasificacion = 'Ingresos altos'
    else:
        clasificacion = 'Ingresos elevados'
    listaClasificacion.append(clasificacion)
#---- Calcular maximo & minimo ----#
mayor = max (listaDolares)
menor = min (listaDolares)
acumulador = 0
for elemento in listaDolares :
    acumulador += elemento
promedio= acumulador/len(listaDolares)
#Este paso solo se hace para redondear el resultado
promedioDolares = round (promedio,2)


#Menu
while (opcion != 4) :
    if (opcion == 1):
        print(mensajeOpcion.format(1))
        #Pregunta conversion
        conversion = input(preguntaConversionDolares)
        if (conversion == 'C'):
            print (listaPesos)
        elif (conversion == 'E') :
            print (listaEuros)
        elif (conversion == 'D') :
            print (mensajeDolares)
            print (listaDolares)
        else :
            print (mensajeErrorMoneda)

    elif (opcion == 2):
        print(mensajeOpcion.format(2))
        print (listaClasificacion)
    elif (opcion == 3):
        print(mensajeOpcion.format(3))
        print ('El ingreso máxima fue', mayor)
        print ('El ingreso mínima fue', menor)
        print ('El ingreso en promedio fue', promedioDolares)
    else:
        print (mensajeErrorNumero)


    #Entrada de la variable de opcion
    opcion = int (input(preguntaMenu))


#Salida del programa
print (mensajeSalida)
