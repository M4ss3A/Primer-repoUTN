## ACTIVIDAD 1
lista_multiplos = list(range(4,101,4))
print(lista_multiplos)


## ACTIVIDAD 2
lista_materias = ["Matematica", "Programacion", "Arquitectura","Organizacion","Ingles"]
penultimo = lista_materias[3]
print(penultimo)
print(type(penultimo))


## ACTIVIDAD 3
lista = []
lista.append(1.1)
lista.append(1.2)
lista.append(1.3)
print(lista)


## ACTIVIDAD 4
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)


## ACTIVIDAD 5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
# Se crea una lista con valores, 
# El programa busca dentro de la lista el valor maximo, 
# Lo elimina de la lista, mediante el termino .remove, 
# Luego imprime resultado.


## ACTIVIDAD 6
numeros = list(range(10,31,5))
print(numeros)
numero_rango = numeros[0:2]
print(numero_rango)


## ACTIVIDAD 7
autos = ["sedan", "polo", "suran", "gol"] 
print(autos)
autos [0] = "Focus"
autos [1] = "Hilux"
print(autos)


## ACTIVIDAD 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


## ACTIVIDAD 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
print(compras)
compras[2].append("Jugo")
compras[1][1] = "Tallarines"
compras[0].remove("pan")
print(compras)


## ACTIVIDAD 10
lista_anidada= [[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)



