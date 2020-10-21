import funciones_archivos as helper
nameFile = 'libro.txt'
helper.agregarLinea ('opinion.txt','Nueva linea')
renglonesLibro = helper.leerArchivos(nameFile) 
print (len(renglonesLibro))

if (len(renglonesLibro)==0):
    print("Es la primera linea que se escribirá en el libro")
    helper.agregarLinea(nameFile,'El día que prograr fué fácil')
else :
    linea = input ('ingrese la linea que desea agregar : \n')
    helper.agregarLinea (nameFile, linea)