import re
import sys

def func(texto):
    # Variable para retornar
    res = ''
    comment1 = ''
    comment2 = ''
    comment3 = ''
    # Busco comentarios con { }
    cond1 = re.findall(r'([^{]*){{,1}[^}]*}{,1}([^{]*)', texto)
    # Encontre y devuelvo
    if (cond1):
        for item in cond1:
            comment1 = comment1 + item[0] + item[1]
        res = comment1
    # Busco comentarios con //
    cond2 = re.findall(r'([^/]*)(//){,1}[^\n]*', comment1)
    # Encontre y devuelvo
    if (cond2):
        for item in cond2:
           comment2 = comment2 + item[0]
        res = comment2
    # Busco comentarios con (* *)
    cond3 = re.findall(r'([^(]*[^*]*)(\(\*){1}[^*]*(\*\)){1}([^(]*)', comment2)
    # Encontre y devuelvo
    if (cond3):
        for item in cond3:
            comment3 = comment3 + item[0] + item[3]
        res = comment3

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
