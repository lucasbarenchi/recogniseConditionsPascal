import re
import sys

def func(texto):
    ifs = re.search('(if )(.*)( then)',texto)
    fors = re.search('(for )(.*)( do)', texto)
    whiles = re.search('(while )(.*)( do)', texto)
    if (ifs.group(2) != None):
        res = ifs.group(2)
    return res

if __name__ == '__main__':

    # Leo parametros
    archivo_entrada = sys.argv[1] # primer argumento pasado al ejecutar el programa
    archivo_salida = sys.argv[2] # segundo argumento pasado al ejecutar el programa

    # Entrada
    f = open(archivo_entrada, 'r') # r indica solo lectura, w escritura, a append
    datos = f.read()
    f.close()

    # Ejecucion y salida
    salida = func(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
