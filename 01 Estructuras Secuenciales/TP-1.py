print("Hola Mundo!")
nombre = input("¿Como te llamas?")
print("¡Hola, " + nombre + "!")
apellido = input("¿Como es tu apellido?")
edad = input("¿Cuantos años tenes?")
zona = input("¿De donde sos?")
print("Soy " + nombre + " "+ apellido + ", tengo " + edad + "," + " y soy de " + zona )

radio = float(input("Ingrese el radio del circulo:"))
pi = 3.14159
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(" Dado el radio, el area es " + str(area) + " , " + "y el perimetro es " + str(perimetro))

minutos = float(input("Ingrese el total de minutos:"))
horas = minutos / 60
print(f"{minutos} equivalen a {horas}")

numero = int(input("Ingrese un numero:"))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))
if num1 == 0 or num2 == 0:
    print("Los numero no pueden ser 0")
else:
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    print(f"El total de la suma es: {suma} ")
    print (f"El total de la resta es: {resta } ")
    print(f"El total de la multiplicacion es: {mult} ")
    print(f"El total de la division es: {div} ")

    peso = float(input("Ingrese su peso:"))
    altura = float(input("Ingrese su altura:"))
    masa = peso / (altura ** 2)
    print(f"Su masa corporal es de {masa}")

gradoc = float(input("Ingrese la temperatura en celsius:"))
gradof = (9 / 5) * gradoc + 32
print(f"La temperatura en Grados Fahrenheit ds {gradof}")

primer = int(input("Ingrese el primer numero:"))
segundo = int(input("Ingrese el segundo numero:"))
tercero = int(input("Ingrese el tercer numero:"))
promedio = (primer + segundo + tercero) / 3
print(f"El promerdio de los numeros es {promedio} ")



