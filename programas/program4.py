import re
import sys

def func(texto):
    # Variable para retornar
    res = ''

    # Busco comentarios con { }, (* *), // y los sustituyo por vacio
    res = re.sub(r'{.*}|(\(\*).*?(\*\))|(//[^\n]*)', '', texto, re.MULTILINE, re.DOTALL)

    return res
if __name__ == '__main__':

    # Leo parametros
    archivo_entrada = sys.argv[1] # primer argumento pasado al ejecutar el programa
    archivo_salida = sys.argv[2] # segundo argumento pasado al ejecutar el programa

    # Entrada
    f = open(archivo_entrada, 'r') # r indica solo lectura, w escritura, a append, r+ lectura y escritura
    datos = f.read()
    f.close()

    # Ejecucion y salida
    salida = func(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
