#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
 #### Cifrado de Nihilist ####

 Ejecución:

    python nihilist.py hello friend myfirstcipher c
    python nihilist.py hello friend 57965543766668646247453566  d

 License: GNU GPLv3
 Solución propuesta por:
   Michaelle Lopez Eudaric
   Juan Antonio Fernández Sánchez
'''


import sys
if len(sys.argv) != 4:
        #El programa no tiene los argumentos necesarios:
        print "Este programa necesita 4 parámetros";
        print "1. Clave 1"  
        print "2. nombre del fichero"
        print "3. c=cifra d=descifra"

else:
    #El programa se ejecuta:
    
    #Independientemente de que se esté cifrando o no la mariz hay que construirla con la clave1 y el abecedario.

    #1.Extraemos la clave del parámetro número 1.
    clave=sys.argv[1]
    #1.Detectamos cualquier elemento repetido en la clave y lo eliminamos.
    claveSinRepetidos = []
    for i in clave:
        if i not in claveSinRepetidos:
            claveSinRepetidos.append(i)

    #2. Creamos una lista con las letras del abecedario inglés |A|=25
    ABCdario = []
    for a in range(97, 123):
        ABCdario.append(chr(a))
    #Eliminamos la j de la lista ya que tiene que ser un abecedario de 25 letras
    del ABCdario[ABCdario.index('j')]

    #3. Añadimos la clave al abecedario, delante de el y eliminando cualquier letra que esté repetida.
    for i in range(len(claveSinRepetidos)-1, -1, -1):
        for letra in ABCdario:
            #Si el abecedario contiene la misma letra, que la que vamos a introducir.
            if letra == claveSinRepetidos[i]:
                #Se elimina la letra del abecedario
                del ABCdario[ABCdario.index(letra)]
        #E insertamos la letra en el abecedario al principio
        ABCdario.insert(0,claveSinRepetidos[i])

    #4. Creamos una matriz (como un diccionario) a la que le introducimos los valores filas-columna y la letra que representan del ABCdario construido

    matriz = {}
    contador = 0
    for a in range(1,6):
        for b in range(1,6):
            matriz[ABCdario[contador]] = int(str(a)+str(b))
            #print str(a)+str(b)+ABCdario[contador]
            contador+=1


    if(sys.argv[3]=='c'):
        print 'Cifrando...'

          #1. Extraemos el mensaje del parámetro 2.
        mensaje=open(sys.argv[2], 'r')
        
        #2.Creamos una lista donde guardaremos el mensaje convertido en números haciendo sustituciones en la matriz.
        textoFinalCifrado = []
        puedeSeguir = True
        while puedeSeguir:
        	letra=mensaje.read(1)
        	if (letra =='' or letra == '\n'):
        		puedeSeguir = False
        	elif (letra !=" "):
        		textoFinalCifrado.append(int(matriz[letra]))

        
        fichero = open ('cifrado.txt', 'w')

        for numero in range(len(textoFinalCifrado)):
            fichero.write(str(textoFinalCifrado[numero]))


    if(sys.argv[3]=='d'):
        print 'Descifrando...'

        '''
        El proceso de desciframiento es muy simple. Esta vez para conocer el tamaño del mensaje original tenemos que analizar el mensaje cifrado
        que nos llega y contabilizar el número de letras que representa, ya que por cada pareja de números (representan una fila y columna enl a matriz)
        será una letra, por tanto una unidad en el mensaje original.
        '''

        #1. Abrir el fichero para lectura.
        numeros= open(sys.argv[2], 'r')
        
        #Leemos nuestro fichero a descifrar
        listaNumerosPasados =[]

        puedeSeguir = True
        while puedeSeguir:
        	pareja = numeros.read(2)
        	if pareja=='' or pareja=='\n':
        		puedeSeguir=False
        	else:
        		listaNumerosPasados.append(int(pareja))
            
        
        #3.Extraemos el texto descifrado sustituyendo en la matriz.
        textoFinalDescifrado = ''
        inv_matriz = {v: k for k, v in matriz.items()}
        for numero in listaNumerosPasados:
            textoFinalDescifrado+=str(inv_matriz[numero])


        #4. Escribimos texto descifrado en el fichero
        fichero = open ('descifrado.txt', 'w')
        for letra in range(len(textoFinalDescifrado)):
        	fichero.write(str(textoFinalDescifrado[letra]))

