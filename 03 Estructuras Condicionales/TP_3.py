## Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad!")

## Actividad 2
NOTA = int(input("Ingrese su nota: "))
if NOTA >= 6:
    print ("Aprobado")
else:
    print("Desaprobado")

## Actividad 3
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par")

## Actividad 4
Edad = int(input("Ingrese su edad: "))
limite_niño = 12
limite_adolecente = 18
limite_adultojoven = 30
if Edad < 12:
    print("Pertenece a la categoria: niños.")
elif Edad < 18:
    print("Pertenece a la categoria: adolescente.")
elif Edad < 30:
    print("Pertenece a la categoria: Adulto- joven.")
else:
    print("Pertenece a la categoria: Adulto.")

## Actividad 5
contrasenia = input("Ingrese contraseña, debe contener entre 8 y 14 caracteres: ")
if 8 <= len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese de entre 8 y 14 caracteres.")

## Actividad 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100)  for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana > moda :
    sesgo = "Sesgo positivo (derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (izquierda)"
else:
    sesgo = "Sin sesgo"
print(f"Numeros aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Resultado_ {sesgo}")

## Actividad 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
    print ("Resultado:", frase)
else:
    print (frase)

## Actividad 8 
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opcion: 1: MAYUSCULAS, 2: MINUSCULAS, 3: PRIMERA MAYUSCULA): ")
if opcion == "1":
    nombre = nombre.upper()
    print(nombre.upper())
elif opcion == "2":
    nombre = nombre.lower()
    print(nombre.lower())
elif opcion == "3":
    nombre = nombre.title()
    print(nombre.title())
else:
    print("Opcion invalida")

    ##Actividad 9
magnitud = float(input("Ingrse la magnitud del terremoto: "))
if magnitud < 3:
        print("La magnitud es MUY LEVE")
elif magnitud >= 3 and magnitud < 4:
        print("La mignitud es LEVE ")
elif magnitud >= 4 and magnitud < 5:
        print("La mignitud es MODERADO")
elif magnitud >= 5 and magnitud < 6:
        print("La magnitud es FUERTE")
elif magnitud >= 6 and magnitud < 7:
        print("La magnitud es MUY FUERTE")
else:
    print("La magnitud es EXTREMA") 

##Actividad 10
hemisferio = input("Ingrese en que hemisferio se encuentra: Norte o Sur: ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))
if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
if hemisferio == "Norte":
    print("Estás en:", estacion_norte)
elif hemisferio == "Sur":
    print("Estás en:", estacion_sur)
else:
    print("Hemisferio no válido.")