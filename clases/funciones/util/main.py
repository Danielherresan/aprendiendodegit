import operaciones_matematicas as opm
import operaciones_strings as ops
#mensajes
mensajeOperacion ='{} las dos entradas'
ops.lineDesignC(12)
valor1 = int (input('Ingrese el valor 1 : '))
valor2 = int (input('Ingrese el valor 2 : '))
ops.lineDesignC(12)
print (mensajeOperacion.format('sumando'))
opm.calculadora(opm.sumar, valor1, valor2)
ops.lineDesignC(12)
ops.lineDesignC(12)
print (mensajeOperacion.format('restando'))
opm.calculadora(opm.restar, valor1, valor2)
ops.lineDesignC(12)
ops.lineDesignC(12)
print (mensajeOperacion.format('multiplicando'))
opm.calculadora(opm.multiplicar, valor1, valor2)
ops.lineDesignC(12)
ops.lineDesignC(12)
print (mensajeOperacion.format('dividiendo'))
opm.calculadora(opm.dividir, valor1, valor2)
ops.lineDesignC(12)

