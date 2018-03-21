import re
import sys

def func(texto):


    return




if __name__ == '__main__':

    # Leo parametros
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    # Entrada
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()

    # Ejecucion y salida
    salida = func(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
