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
if len(sys.argv) != 5:
        #El programa no tiene los argumentos necesarios:
        print "Este programa necesita 4 parámetros";
        print "1. Clave 1"
        print "2. Clave 2"
        print "3. Mensaje"
        print "4. c=cifra d=descifra"
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

    if(sys.argv[4]=='c'):
        print 'Cifrando...'

        '''
        Para cifrar necestamos una segunda clave. Con esta segunda clave cramos un texto tan largo como el mensaje a cifrar compuesto
        de ciclos de la clave hasta el tamaño del mensaje. Una vez conseguido este mensaje de ciclos de la clave ambos, tanto mensaje original
        como la clave en ciclos (ambos del mismo tamaño) los pasamos por la matriz de sustitución para que convierta la letras en números
        y después sumamos esos números. El resultado de esa suma es el texto cifrado y será lo que devuelva el programa.
        '''

        #1. Extraemos el mensaje del parámetro 3.
        mensaje=sys.argv[3]
        #Obtenemos su tamaño.
        tamMensaje=len(mensaje)

        #2.Creamos una lista donde guardaremos el mensaje convertido en números haciendo sustituciones en la matriz.
        mensajeEnNumeros = []
        for letra in mensaje:
            #print letra + str(matriz[letra])
            if (letra !=" "):
                mensajeEnNumeros.append(int(matriz[letra]))
            #print mensajeEnNumeros

        #3. Extraemos la segunda clave del parámetro 2
        clave2 = sys.argv[2]
        #Obtenemos su tamaño.
        tamClave2=len(clave2)

        #4. Construimos una cadena que sea la clave en bucle hasta completar el tamaño del mensaje original.
        #Ahora tenemos que hacer una cadena del mismo tamaño que la cadena del mensaje con ciclos de la clave2.
        contador=0;
        #¿Cuantas veces hay que multiplicar? Nos pasamos siempre, de resto o no la división.
        numDiv=(tamMensaje/tamClave2)+1
        #Aquí el texto
        clave2enCiclos=clave2*numDiv
        #Cortamos de la clave ciclada el número de caracteres del tamaño del mensaje original a cifrar y todo lo guardarmos en mensaje2
        mensaje2=[]
        for a in range(tamMensaje):
            mensaje2.append(clave2enCiclos[a])

        #5. Ahora hay que traducir a números el mensaje 2 usando la matriz, como se hizo con el mensaje original, en el paso 2
        mensaje2EnNumeros = []
        for letra in mensaje2:
            #print letra + str(matriz[letra])
            mensaje2EnNumeros.append(int(matriz[letra]))

        #6. Una vez que tenemos dos listas de números que representan ambos mensajes (ambos del mismo tamaño siempre) realizamos la suma:
        #Lo almacenamos en textoFinalCifrado
        textoFinalCifrado = []
        for a in range(len(mensajeEnNumeros)):
            suma=mensajeEnNumeros[a]+mensaje2EnNumeros[a]
            textoFinalCifrado.append(suma)


        print "Texto cifrado: "

        for numero in range(len(textoFinalCifrado)):
            print textoFinalCifrado[numero],


    if(sys.argv[4]=='d'):
        print 'Descifrando...'

        '''
        El proceso de desciframiento es muy simple. Esta vez para conocer el tamaño del mensaje original tenemos que analizar el mensaje cifrado
        que nos llega y contabilizar el número de letras que representa, ya que por cada pareja de números (representan una fila y columna enl a matriz)
        será una letra, por tanto una unidad en el mensaje original y en el mensaje2 que se necesita componer con ciclos de la clave2 para realizar,
        en este caso, una resta.
        '''

        #1. Obtenemos el tamaño del mensaje a descifrar.
        numeros=sys.argv[3]
        tamMensaje=len(numeros)/2

        #2. Conocido el tamaño, creamos un mensaje de igual tamaño con ciclos usando como palabra la clave2
        #Para ello extraemos la segunda clave del parámetro 2 y obtenemos su tamaño.
        clave2 = sys.argv[2]
        tamClave2=len(clave2)
        contador=0;
        numDiv=(tamMensaje/tamClave2)+1
        clave2enCiclos=clave2*numDiv
        #Creamos el mensaje2 como hicimos antes.
        mensaje2=[]
        for a in range(tamMensaje):
            mensaje2.append(clave2enCiclos[a])

        #3.Pasamos tanto el mensaje2 a números para poder restarlo al mensaje original:
        mensaje2EnNumeros = []
        for letra in mensaje2:
            #print letra + str(matriz[letra])
            mensaje2EnNumeros.append(int(matriz[letra]))

        #4.Restamos los números extraidos del texto cifrado pasado divididos en grupos de dos cifras - el mensaje2 en números.

        #Para ello extremos los números de parámetro pasado
        size=len(numeros)/2
        listaNumerosPasados =[]

        for a in range(size):
            listaNumerosPasados.append(int(numeros[0:2]))
            numeros=numeros[2:]

        #Una vez que tenemos los número en una lista procedemos a la resta de los numeros pasados menos los del mensaje2
        numerosFinales = []
        #listaNumerosPasados y mensaje2EnNumeros tienen el mismo tamaño.
        for numero in range(len(listaNumerosPasados)):
            numerosFinales.append(listaNumerosPasados[numero]-mensaje2EnNumeros[numero])

        #5.Extraemos el texto descifrado sustituyendo en la matriz.
        textoFinalDescifrado = ''
        inv_matriz = {v: k for k, v in matriz.items()}
        for numero in numerosFinales:
            textoFinalDescifrado+=str(inv_matriz[numero])

        #6.Imprimos el mensaje:
        print 'Texto descifrado: \n' + textoFinalDescifrado
