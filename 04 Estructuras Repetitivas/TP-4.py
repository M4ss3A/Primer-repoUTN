## ACTIVIDAD 1

for numero in range(1, 100 + 1):
    print(numero)

## ACTIVIDAD 2 

numero = int(input("Ingrese un numero entero: "))
while numero > 0:
    cantidad = len(str(numero))
    print("El numero ingresado tiene", cantidad , "de digitos.")
    break


## ACTIVIDAD 3

inicio = int(input("Ingrese un numero:"))
fin = int(input("Ingrese otro numero:"))
if inicio > fin:
    inicio, fin = fin, inicio
sumatoria = 0
for i in range (inicio + 1, fin):
    sumatoria += i 
print("La suma entre los comprendidos de los numeros es:", sumatoria)

## ACTIVIDAD 4

sumatoria = 0
while True:
    numero = int(input("Ingrese un numero e ingrese 0 para finalizar: "))
    if numero == 0:
        break
        sumatoria += numero
print("El total acumulado es: ", sumatoria)


## ACTIVIDAD 5 

import random
numero_secreto = random.randint (0, 9)
intentos = 0
correcto = False
while not correcto :
    intento = int(input("Adivina el numero secreto ente 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        correcto = True
        print("ADIVINASTEE!, En el intento numero", intentos, "Felicitaciones!")
    else:
        print("Incorrecto, intente nuevamente. ")


## ACTIVIDAD 6

for numero in range (100, -1, -1):
    if numero % 2 == 0:
        print(numero)


## ACTIVIDAD 7

n = int(input("Ingresa un numero entero que sea positivo: "))
for i in range (n + 1):
    suma += i
    print("La suma de los numeros entre 0 y ", n , "es : ", suma)


    ## ACTIVIDAD 8

cantidad = int(input("¿Cuantos numeros desea ingresar?"))
pares = impares = positivos = negativos = 0
for _ in range (cantidad):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1 
    else:
        numero % 2 != 0
        impares += 1
    if numero > 0:
        positivos += 1
    else:
        numero > 0
        negativos += 1
print("Los numeros pares son: ", pares)
print("Los numeros impares son: ", impares)
print("Los numeros positivos son: ", positivos)
print("La cantidad de numeros negativos son: ")


## ACTIVIDAD 9

cantidad = int(input("¿Cuantos numeros desea ingresar? "))
suma = 0
for _ in range (cantidad):
    numero = int(input("Ingrese un numero: "))
    suma += numero
media = suma / cantidad
print("La media de los numeros es:", media)


## ACTIVIDAD 10 

numero = int(input("Ingrese un numero: "))
numero_invertido = 0 
while numero > 0:
    cant = numero % 10
    numero_invertido = numero_invertido * 10 + cant
    numero //= 10
print("Numero invertido: ", numero_invertido)
