#Objetivo
#Descifrar los "Mensajes Secretos de una Carta de Amor" usando strings, indexación, slicing, stride y strings de múltiples líneas en Python.
#Instrucciones:
#
#Se te proporcionará una carta de amor que contiene tres párrafos, cada uno con un mensaje secreto oculto.
#
#Tu tarea es escribir un programa en Python que utilice técnicas de indexación, slicing y stride para descifrar estos mensajes.

#Cada párrafo tiene un patrón de codificación diferente:

#En el primer párrafo, el mensaje secreto está formado por cada decimoctavo (18) caracter, comenzando desde el segundo caracter.

#En el segundo párrafo, el mensaje secreto se encuentra entre el caracter 138 y 147 de la cadena de texto.

#En el tercer párrafo, el mensaje secreto está formado por las letras que se encuentran en las siguientes posiciones de la cadena de texto:

#Primera letra: posición 125

#Segunda letra: posición 94

#Tercera letra: posición 35

#Cuarta letra: posición 107

#Quinta letra: posición 20

#Sexta letra: posición 1

#Usa print para mostrar los mensajes secretos decodificados.


parrafo1 = "Cada dia te quiero mas y nunca lo he olvidado."

parrafo2 = "En el corazón de una historia de amor tecnológica, Lucas y Carla compartían su pasión por la programación. Cada día, mientras aprendían a programar, sus corazones se sincronizaban con cada línea de código."

parrafo3 = "En cada amanecer, veo el brillo de tus ojos; en cada atardecer, siento el calor de tu abrazo; y en cada noche estrellada, me pierdo en el infinito de tu amor."

#mi forma
print()

print(parrafo1[1::18])

print(parrafo2[138:147])

print(parrafo3[125],parrafo3[94],parrafo3[35],parrafo3[107],parrafo3[20],parrafo3[1])

print(parrafo1[1::18],parrafo2[138:147],parrafo3[125],parrafo3[94],parrafo3[35],parrafo3[107],parrafo3[20],parrafo3[1])

print()
print()


#Forma del profesor

mensaje_secreto1=parrafo1[1::18]
mensaje_secreto2=parrafo2[138:147]
mensaje_secreto3_1 = parrafo3[125]
mensaje_secreto3_2 = parrafo3[94]
mensaje_secreto3_3 = parrafo3[35]
mensaje_secreto3_4 = parrafo3[107]
mensaje_secreto3_5 = parrafo3[20]
mensaje_secreto3_6 = parrafo3[1]

print("mensaje secreto decodificado")
print("Mensaje secreto 1:")
print(mensaje_secreto1)
print("Mensaje secreto 2:")
print(mensaje_secreto2)
print("Mensaje secreto 3:")
print(mensaje_secreto3_1)
print(mensaje_secreto3_2)
print(mensaje_secreto3_3)
print(mensaje_secreto3_4)
print(mensaje_secreto3_5)
print(mensaje_secreto3_6)

