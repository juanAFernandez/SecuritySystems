#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
 License: GNU GPLv3
 Solución propuesta por:
   Michaelle Lopez Eudaric
   Juan Antonio Fernández Sánchez
'''

import sys
if len(sys.argv) != 2:
        #El programa no tiene los argumentos necesarios:
        print "Este programa necesita 1 parámetro"
        print "1. Fichero de texto fuente"
else:
    #Ejecución del programa:

    #1.Abrimos el fichero cogiendo el parámetro pasado.
    fichero = open(sys.argv[1], 'r')

    #2.Recorremos todo el texto extrayendo parejas de dos.

    #creamos un diccionario

    tabla={}

    puedeSeguir =True
    while puedeSeguir:
        pareja = fichero.read(2)

        #El valor no existe en el diccionario, lo añadimos:
        if(tabla.get(pareja)==None):
            tabla[pareja]=1
        #Si ya existe aumentamos en uno el valor de esta clave:
        else:
            tabla[pareja]=tabla[pareja]+1
        #print pareja
        if pareja=='':
            puedeSeguir=False


    #Eliminamos metacaracteres leidos desde el fichero.

    print tabla

    #n.Cerramos el fichero
    fichero.close()
