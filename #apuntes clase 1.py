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

