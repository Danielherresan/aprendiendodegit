def leerArchivos(nombreArchivo) :
    listaRenglones = []
    with open (nombreArchivo, encoding  = 'UTF-8') as lineas:
        for line in lineas :
            print (line)
            listaRenglones.append(line)
    return listaRenglones

def crearArchivos (nombreArchivo) : 
    archivo = open (nombreArchivo,'w', encoding='UTF-8')
    archivo.close
    return None

def agregarLinea (nombreArchivo, linea): 
    archivo = open (nombreArchivo,'a', encoding='UTF-8')
    archivo.write(f'\n{linea}')
    archivo.close()
    return None