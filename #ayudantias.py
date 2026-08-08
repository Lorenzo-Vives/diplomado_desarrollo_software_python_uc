#ayudantía 2

lista = []

dicto = {
    "A": ["Alarma"],
    "B": ["Bote", "Barco", "Bolso"],
    "C": ["Calabaza"]
}


dicto["D"] = ["Delta"]

dicto["A"].append("Altura") #asi agrego a una lista, en una determinado elemento

lista.append(999)#append agrega un elemento al final de la lista

print(dicto)

for elemento in lista:
    if elemento == 1213:
        print(elemento)

for i in range(0, len(lista)-1):
    pass
    #print(lista[i +1])




#------------
#miniproyecto
#------------

#transformar lista a diccionario