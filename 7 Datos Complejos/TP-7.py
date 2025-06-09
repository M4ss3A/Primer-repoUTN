#ACTIVIDAD1
#Diccionario
precios_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450}
print("Diccionario: ", precios_frutas)
#Agregar nuevar Key-Value
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario actualizado: ", precios_frutas)

#ACTIVIDAD2
#Modificacion de valor
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print("Valores actualizados: ", precios_frutas)

#ACTIVIDAD3
#Lista de frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas: ", lista_frutas)

#ACTIVIDAD4
# Programa que pide los datos y los almacena 
Contactos = {}
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto:{i + 1} ")
    numero = input(f"Ingresa el numero de {nombre}: ")
    Contactos[nombre] = numero
#Permiten consultar e imprimir la solicitud
consulta = input("Ingresa el nombre que quiere consultar: ")
if consulta in Contactos:
    print(f"El numero de {consulta} es: {Contactos[consulta]}")
else:
    print("Ese contacno no existe.")

#ACTIVIDAD5
#Solicitar a usuario que ingrese una frase e imprimir
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] +=1
    else:
        recuento[palabra] = 1
print("Palabras unicas: ", palabras_unicas)
print("Recuento: ", recuento)

#ACTIVIDAD6
#Permite el ingreso de alunmos
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas_str = input(f"Ingrese las 3 notas de {nombre}, separadas por comas: ")
    notas = tuple(map(int, notas_str.split(",")))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Notas = {notas}, Promedio = {promedio: .2f}")

#ACTIVIDAD7
#Set de numeros e impresion de aprobacion
Parcial1 = {'Martina','Camila', 'Alberto', 'Gaston', 'Paula'}
Parcial2 = {'Camila', 'Pablo', 'Matias', 'Mia', 'Alberto', 'Paula'}
ambos = Parcial1 & Parcial2
Solo_uno = Parcial1 ^ Parcial2
al_menos_uno = Parcial1 | Parcial2
print("Aprobaron ambos parciales: ", ambos)
print("Aprobaron solo uno de los parciales: ", Solo_uno)
print("Aprobaron al menos uno de los parciales: ", al_menos_uno)

#ACTIVIDAD8
#Diccionario y operaciones
stock = {'teclado' : 20,'monitor': 14, 'auriculares': 31}
producto = input("Ingrese el nombre el producto: ")
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")

    agregar = input("¿Desea aregar mas unidaddes?(s/n)")
    if agregar.lower() == "s":
        cantidad = int(input("¿Cuantas unidades queres agregar?"))
        stock[producto] += cantidad
        print(f"Nuevo Stock de {producto}: {stock[producto]}")
else:
    print(f"{producto} no existe existe en el Stock.")
    agregar = input("¿Desea agregar producto nuevo? (s/n):")
    if agregar.lower() == "s":
        cantidad = int(input("¿Cuantas unidades?: "))
        stock[producto] = cantidad
        print(f"Producto: {producto} agregado con Stock: {cantidad}")

#ACTIVIDAD9
# Agenda con fecha y hora
agenda = {("Lunes", "09:00"): "Reunión", ("Martes", "11:00"): "Presentación", ("Miércoles", "16:00"): "Clase de inglés"}
dia = "Lunes"
hora = "09:00"
evento = agenda.get((dia, hora), "No hay evento agendado")
print(f"Evento el {dia} a las {hora}: {evento}")

#ACTIVIDAD10
# Paises y sus capitales
# Diccionario original: país -> capital
paises_a_capitales = {"Argentina": "Buenos Aires","Francia": "París","Italia": "Roma"}
print(paises_a_capitales)
capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}
print(capitales_a_paises)

