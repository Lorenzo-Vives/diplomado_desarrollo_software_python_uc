################################################################################
################################ MINIPROYECTO 1 ################################
################################################################################
import pprint
import utilidades

# Instrucciones: A continuación se presentan 6 funciones, las cuáles están vacías o incompletas.
# Tu trabajo es completarlas según las especificaciones del enunciado.
# Podrás probar tus funciones modificando la sección final del código y ejecutando
# este programa mediante el comando "python3 main.py"
tr = utilidades.cargar_csv("transacciones.csv")

print(tr)
# FUNCIÓN 1: GENERAR HISTORIAL DEL BANCO
# A partir de la lista de transacciones sin procesar, debes retornar un diccionario,
# donde las llaves sean el RUT de la persona y el valor otro diccionario,
# con el formato { nombre, transacciones }
def crear_historial_banco(nombre):
    # NO MODIFICAR
    transacciones_sin_procesar = utilidades.cargar_csv(nombre)
    # AHORA COMPLETA LA FUNCIÓN, BORRANDO EL "pass" Y ESCRIBIENDO LO QUE FALTA.
    historial = {}
    for rut in transacciones_sin_procesar [1:]:
            listarut = rut.split(",")
            rut = listarut[0] 
            nombre = listarut[1]
            transaccion = listarut[2]
            monto = listarut[3]
            if rut in historial: #si existe el rut
                historial[rut]["transacciones"]["transaccion"].append(transaccion) #lista dentro del dicto pra agregar nuevos datos si es necesario
                historial[rut]["transacciones"]["monto"].append(monto) #lo mismo
            else:  #si no
                historial[rut] = {
                "rut": rut,
                "nombre": nombre,
                "transacciones": {
                    "transaccion": [transaccion],
                    "monto": [monto]
                }
            }
    return historial 
#testeo
historial = crear_historial_banco("transacciones.csv")
#print(historial["20.415.740-5"])

# FUNCION 2: LISTAR CLIENTES DEL BANCO
# En base al historial creado en el paso anterior, deberás extraer los nombres
# de todos los clientes del banco y retornarlos en una lista

def listar_clientes(historial):
    clientes = []
    for info in historial.values(): #sacado de la ayudantía
        clientes.append(info["nombre"])
    return clientes

#testeo
#listar_clientes(historial)


# FUNCION 3: REGISTRAR CLIENTE EN EL BANCO
# Dado un rut y nombre del cliente, registrarlo en el historial.
# Si el cliente ya existe, debes avisar.
def registrar_cliente(historial, rut, nombre):
    if rut in historial:
        print("El cliente ya existe en la base")
    else: 
        historial[rut] = { #mismo q arriba
            "rut": rut,
            "nombre": nombre,
            "transacciones": {
                 "transaccion": [],
                 "monto": []
             }
        }
        print(f"registrado el cliente nombre: {nombre}, rut {rut}")
#testeo
#registrar_cliente(historial, "20.415.740-5", "Nicolás Contreras Herrera")
#registrar_cliente(historial, "20.557.560-k", "Lorenzo Vives")

# FUNCION 4: ENTREGAR HISTORIAL DE TRANSACCIONES DE UN CLIENTE
# Dado el rut de un cliente, debes retornar el historial de transacciones del
# cliente en el formato pedido, junto con un resumen.
# Además, debes enviar un mensaje especial si el RUT ingresado no es cliente
def entregar_historial_cliente(historial, rut):
    if rut not in historial: #not in sacado de la ayudantía
        print("el cliente no está registrado en la base")
        return
    cartola = historial[rut]
    print(f"rut: {cartola['rut']}")
    print(f"nombre: {cartola['nombre']}")
    print(f"transacciones: {cartola['transacciones']['transaccion']}") #dos [] ya que quiero perdir la lista
    print(f"monto: {cartola['transacciones']['monto']}")

#testeo
#entregar_historial_cliente(historial,"20.557.560-k")

# FUNCION 5: AGREGAR O QUITAR DEPOSITO AL USUARIO
# Dado un rut, un monto y una transacción que puede ser un deposito o un retiro
# Debes añadir la transacción a la cuenta del cliente, siguiendo las restricciones:
# - El cliente debe existir en el banco.
# - El tipo de transacción debe ser o "deposito" o "retiro"
# - El monto a agregar debe ser un numero entero y positivo mayor a 0.
# - Si la transacción es un retiro, debes verificar que el usuario tiene suficiente saldo en la cuenta.
# - En caso de no cumplir alguna de estas reglas, debes avisar cuál fue el problema.
def nueva_transaccion(historial, rut, monto, transaccion="deposito"):
    if rut not in historial:
        print(f"el cliente rut: {rut} no existe en la base")
        return
    if transaccion not in ("deposito", "retiro"):
        print(f"operación {transaccion} no permitida")
        return
    if not isinstance(monto, int) or isinstance(monto, bool):#isinstance: Return whether an object is an instance of a class or of a subclass thereof.
        print("el monto no es un n° entero")
        return                      
    if monto <= 0:
        print("el monto debe ser mayor a 0")
        return
    saldo = 0 #al final si creé el saldo pq sino era muy enredado calcular
    transacciones = historial[rut]["transacciones"]["transaccion"]
    montos = historial[rut]["transacciones"]["monto"]

    for i in range(len(transacciones)):
        if transacciones[i] == "deposito":
            saldo += int(montos[i])
        elif transacciones[i] == "retiro":
            saldo -= int(montos[i])

    if transaccion == "retiro": #aquí no tengo una col de saldo, es dificil evaluarlo
        if saldo < monto:
            print("no hay suficientes fondos para el retiro")
            return
        historial[rut]["transacciones"]["transaccion"].append(transaccion) 
        historial[rut]["transacciones"]["monto"].append(monto) 
        print("retiro realizado correctamente")
       
    else: 
        historial[rut]["transacciones"]["transaccion"].append(transaccion)
        historial[rut]["transacciones"]["monto"].append(monto)  
        print("depósito fue realizado correctamente")

#testeo
#nueva_transaccion(historial, "20.557.560-k",10000, transaccion ="deposito")
#nueva_transaccion(historial, "20.557.560-k",40000, transaccion ="retiro")

# FUNCION 6: CREAR MENÚ DE INTERACCIÓN
# Debes crear un menú con el que se pueda interactuar con tu programa. Para esto debes:
# - Imprimir un listado de las posibles opciones de tu menú, incluyendo una para terminar el programa.
# - Permitir que el usuario ingrese una opción mediante la terminal.
# - Si la opcion es válida (una de las posibles), pedir los argumentos faltantes por consola y ejecutarla.
# - Si la opción no está en el listado posible, avisar al usuario.
# - El menú debe funcionar de manera infinita (es decir, volver a pedir opciones luego de ejecutar
#   una acción) hasta que se seleccione la opción de terminar el programa. En ese caso, la función debe finalizar.
def programa_interactivo(historial):
    opciones = {
        "1": "listado de clientes",
        "2": "registrar nuevo cliente",
        "3": "historial del cliente",
        "4": "nueva transacción",
        "-1": "salir del programa" #sacado de la ayudantía
    }
    while True:
        print("\nBienvenido a la base de datos bancaria. ¿Cuál es la acción que deseas realizar?")
        for clave, texto in opciones.items():
            print(f"[{clave}]{texto}")
        
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1": 
            print(listar_clientes(historial_banco))
                    
        elif opcion == "2":
            rut = input("Ingrese el rut del cliente: ").strip()
            nombre = input("Ingrese el nombre completo del cliente: ").strip()
            registrar_cliente(historial_banco, rut, nombre)

        elif opcion == "3":
            rut = input("Ingrese el rut del cliente: ").strip()
            entregar_historial_cliente(historial_banco, rut)

        elif opcion == "4":
            rut = input("Ingrese el rut del cliente: ").strip()
            monto = input("Ingrese el monto de la operación: ").strip()

            if monto.lstrip("-").isdigit():
                monto = int(monto) 
                transaccion = input("Ingrese la transaccion a realizar (deposito/retiro): ").strip()
                nueva_transaccion(historial_banco, rut, monto, transaccion)
            else: 
                print("el monto debe ser un n° entero")
        
        elif opcion == "-1":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")



# ESTA SECCIÓN TE PERMITE PROBAR TU CÓDIGO
if __name__ == "__main__":
    # CAMBIAR ENTRE TRUE Y FALSE SI DESEAS PROBARLO DE FORMA INTERACTIVA MEDIANTE
    INTERACTIVO = True

    historial_banco = crear_historial_banco("transacciones.csv")
    # NO MODIFICAR
    if historial_banco:
        if INTERACTIVO:
            programa_interactivo(historial_banco)
        else:
            # Primero la carga de datos
            print("\nHistorial cargado. Mostrando información de un cliente:")
            pprint.pp(historial_banco["20.415.740-5"])
            print("\nMostrando lista de clientes del banco")
            listar_clientes(historial_banco)
            print("\nRegistrando un cliente nuevo")
            print(registrar_cliente(historial_banco, "12.345.678-9", "Juan Sotomayor"))
            print("\nBuscando el historial de algunos clientes...")
            entregar_historial_cliente(historial_banco, "12.345.678-9")
            entregar_historial_cliente(historial_banco, "8.112.034-K")
            entregar_historial_cliente(historial_banco, "8.765.432-1")
            print("\nRealizando transacciones en el banco")
            nueva_transaccion(historial_banco, "12.345.678-8", 100000, "retiro")
            nueva_transaccion(historial_banco, "12.345.678-9", 100000, "retiro")
            nueva_transaccion(historial_banco, "12.345.678-9", 17800.15, "retiro")
            nueva_transaccion(historial_banco, "12.345.678-9", 17800, "deposito")
            nueva_transaccion(historial_banco, "12.345.678-9", 50000, "deposito")
            nueva_transaccion(historial_banco, "12.345.678-9", 10000, "retiro")
    else:
        print("Llena primero la función crear_historial_banco antes de probar tu código.")


#preguntar al ayudante si es necesario tener el saldo en el menú 