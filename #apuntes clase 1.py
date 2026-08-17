#apuntes clase 1

#-------------------
# flujo: if, for & while
#-------------------





#-------------------
#funciones
#-------------------
nombre = "Lorenzo"

def saludo(nombre, repeticiones=1, mayusculas=False):

    for i in range(repeticiones):

        mensaje = "Hola, " + nombre + "!"

        if mayusculas:

            mensaje = mensaje.upper()

        print(mensaje)

saludo("Lorenzo",3)



saludo('Luis') # Nombre por posición, resto por defecto
saludo('Ana', 3) # Nombre y repeticiones por posición
saludo(nombre='Pedro') # Nombre por keyword
saludo(nombre='Carla', mayusculas=True) # Uso de keyword
saludo('Marta', mayusculas=True) # Posición y keyword

help(int)




#-------------------
#listas de datos secuenciales
#-------------------

list() #tiene un orden, mutable y permite combinar distintos tipos de datos

num = [5,12,32,45]
print(num)
print(num[0])
print(num[-2]) #penultimo elemento
print(num[1:3])
print(num[0:4:2])

#lenght
len(num)

# Agrega un valor al final de una lista.
num.append(10)

# Quita de la lista el valor ubicado en la posición indicada
# y lo retorna.
valor_eliminado = num.pop(2)
# Ordena los elementos dentro de la lista.
num.sort()

# Invierte el orden actual de los elementos de la lista.
num.reverse()

# Retorna el índice de la primera aparición del valor en la lista.
# Genera una excepción ValueError si el valor no está presente.
posicion = num.index(2)
# Retorna la cantidad de veces que el valor aparece en la lista.
cantidad = num.count(2)

#listas se pueden sumar con +
numeros = [1, 2, 3]
letras = list('abc')
numeros + letras
numeros * 3
print(numeros + letras)
4 in numeros


#tuplas, valores fijos

Tupla = (20, "lorenzo", 26, 1.2, [10,20,30],20)


Tupla.index(26)  # Busca la primera aparición de valor en la tupla y devuelve su índice.                                                   |

Tupla.count(20)  #Cuenta cuántas veces aparece valor en la tupla.

#tupla también se pueden sumar





#------------------------------------------------------------------------------
# apuntes clase 3
#------------------------------------------------------------------------------

#librerías

import math #librería math, permite hacer operaciones + complejas

math.cos(math.pi / 4)

math.sqrt(2) / 2

import random #librería random permite meter aleatoriedad

random.random()

random.choice(["manzana", "pera", "naranja", "platano", "melon", "uva"]) #choice agarra un obj random de la lista

import statistics #lib para sacar descriptivos

data = [2.75, 1.50, 1.75, 2.3, 2.15, 0.85]

#media, mediana y varianza
statistics.mean(data)

statistics.median(data)

statistics.variance(data)


from pathlib import Path #lib para working directory y rutas

ruta = Path(".") #creamos ruta

ruta.resolve() #le pedimos la ruta

ruta.exists() #boleando q preugnta si la ruta existe

for elemento in ruta.iterdir(): #permite buscar los elementos de la ruta
    print(elemento)f

for i in ruta.iterdir():
    print(i)

import json #convertir a diccionario json

datos = {"nombre": "Valeria", "edad":31}

textos = json.dumps(datos)
print(textos)

recuperado = json.loads(textos)
print(recuperado["nombre"])
