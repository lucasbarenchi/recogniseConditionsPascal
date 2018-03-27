import re
import sys

def func(texto):
    # Variables para retornar
    resif = 'if: \n'
    resfor = 'for: \n'
    reswhile = 'while: \n'
    res = ''

    cond = re.findall(' *(if )(.*) then *| *(for )(.*) do *| *(while )(.*) do *', texto)

    if (cond):
        for item in cond:
            if (item[0] == 'if '):
                resif = resif + item[1] + '\n'
            if (item[2] == 'for '):
                resfor = resfor + item[3] + '\n'
            if (item[4] == 'while '):
                reswhile = reswhile + item[5] + '\n'
        if (not (resif == 'if: \n')):
            res = res + resif
        if (not (resfor == 'for: \n')):
            res = res + resfor
        if (not (reswhile == 'while \n')):
            res = res + reswhile
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
