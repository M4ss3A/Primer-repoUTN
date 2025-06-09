## ACTIVIDAD 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


## ACTIVIDAD 2
def saludar_usuario(nombre):
    print(f"Hola,{nombre}!")
nombre_ingresado = input("¿Como es tu nombre?: ")

saludar_usuario(nombre_ingresado)


## ACTIVIDAD 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


## ACTOIVIDAD 4
import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area es {area:.2f}")
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro es {perimetro:.2f}")

radio = float(input("Por favor, ingrese el radio: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


## ACTIVIDAD 5 
def segundos_a_horas (segundos):
    return segundos / 3600

seg = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(seg)

print(f"{seg} segundos equivalen a {horas:.2f} horas.")


## ACTIVIDAD 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un numero del 1 al 10: "))
tabla_multiplicar(numero)


## ACTIVIDAD 7
def operaciones_basicas(a,b):
    suma = a + b
    print(f"SUMA: {suma}")
    resta = a - b
    print(f"RESTA: {resta}")
    multi = a * b
    print(f"MULTIPLICACION: {multi}")
    if b != 0:
        div = a / b
        print(f"DIVISION: {div}")
    else: print("No se puede dividir")

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

operaciones_basicas(a,b)


## ACTIVIDAD 8
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    print(f"Su imc es: {imc:.2f}")
    
peso = float(input("Ingrese su peso: "))
altura = float (input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)

## ACTIVIDAD 9 
def celsius_a_fahrenheit(celsius):
    fahren = (celsius * 1.8) + 32 
    print(f"La temperatura ingresadad corresponde a {fahren:.2f}°F.")

celsius = float(input("Ingrese la temperatura en GRADOS CELSIUS: "))

celsius_a_fahrenheit(celsius)

## ACTIVIDAD 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3 
    print(f"El promedio es: {promedio:}") 
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el teercer numero: "))

calcular_promedio(a, b, c)


