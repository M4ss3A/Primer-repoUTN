#ACTIVIDAD1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
         return n * factorial(n-1)

def factoriales(hasta):
    for i in range(1,hasta + 1):
        print(f"{i}! = {factorial(i)}")

num = int(input("Ingrese un numero entero positivo: ")) 
factoriales(num)

#ACTIVIDAD2
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

n = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))
mostrar_serie_fibonacci(n)

#ACTIVIDAD3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


#ACTIVIDAD4
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n)

n = int(input("Ingrese un número entero positivo: "))
print(f"Representación binaria de {n}: {convertir_a_binario(n)}")

#ACTIVIDAD5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print("¿Es palíndromo?", es_palindromo(palabra))


#ACTIVIDAD6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {n} es {suma_digitos(n)}")

#ACTIVIDAD7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#ACTIVIDAD8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
