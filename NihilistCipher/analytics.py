#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
 License: GNU GPLv3
 Solución propuesta por:
   Michaelle Lopez Eudaric
   Juan Antonio Fernández Sánchez
'''

'''
Requiere un string.
'''
def analytics(mensaje):
    #2.Recorremos todo el texto extrayendo parejas de dos.
    #creamos un diccionario
    tabla={}
    #Tenemos que extraer los números de dos en dos y formar con ellos un entero.
    while len(mensaje)!=0:
        dosEnteros=int(mensaje[0:2]) #Extraemos dos cifras del string de números convirtiéndolo en un entero.
        mensaje=mensaje[2:] #Recortamos el string de números quitando los dos primeros números.

        #El valor no existe en el diccionario, lo añadimos:
        if(tabla.get(dosEnteros)==None):
            tabla[dosEnteros]=1
        #Si ya existe aumentamos en uno el valor de esta clave:
        else:
            tabla[dosEnteros]=tabla[dosEnteros]+1


    #Eliminamos metacaracteres leidos desde el fichero.
    if tabla.get(''):
        del tabla['']
    if tabla.get('\n'):
        del tabla['\n']

    print tabla
    return tabla



import sys
if len(sys.argv) != 2:
        #El programa no tiene los argumentos necesarios:
        print "Este programa necesita 1 parámetro"
        print "1. Fichero de texto fuente"
else:
    #Ejecución del programa:

    #1.Abrimos el fichero cogiendo el parámetro pasado.
    fichero = open(sys.argv[1], 'r')

    #2. Creamos un string con el contenido del fichero.
    cadena=""
    for line in fichero:
        cadena+=line
    #3. Llamamos a analytics
    analytics(cadena)


    #4.Cerramos el fichero
    fichero.close()
