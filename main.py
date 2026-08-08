################################################################################
################################ MINIPROYECTO 1 ################################
################################################################################
import pprint
import utilidades

# Instrucciones: A continuación se presentan 6 funciones, las cuáles están vacías o incompletas.
# Tu trabajo es completarlas según las especificaciones del enunciado.
# Podrás probar tus funciones modificando la sección final del código y ejecutando
# este programa mediante el comando "python3 main.py"

# FUNCIÓN 1: GENERAR HISTORIAL DEL BANCO
# A partir de la lista de transacciones sin procesar, debes retornar un diccionario,
# donde las llaves sean el RUT de la persona y el valor otro diccionario,
# con el formato { nombre, transacciones }
def crear_historial_banco(nombre):
    # NO MODIFICAR
    transacciones_sin_procesar = utilidades.cargar_csv(nombre)
    # AHORA COMPLETA LA FUNCIÓN, BORRANDO EL "pass" Y ESCRIBIENDO LO QUE FALTA.
    pass


# FUNCION 2: LISTAR CLIENTES DEL BANCO
# En base al historial creado en el paso anterior, deberás extraer los nombres
# de todos los clientes del banco y retornarlos en una lista
def listar_clientes(historial):
    pass


# FUNCION 3: REGISTRAR CLIENTE EN EL BANCO
# Dado un rut y nombre del cliente, registrarlo en el historial.
# Si el cliente ya existe, debes avisar.
def registrar_cliente(historial, rut, nombre):
    pass


# FUNCION 4: ENTREGAR HISTORIAL DE TRANSACCIONES DE UN CLIENTE
# Dado el rut de un cliente, debes retornar el historial de transacciones del
# cliente en el formato pedido, junto con un resumen.
# Además, debes enviar un mensaje especial si el RUT ingresado no es cliente
def entregar_historial_cliente(historial, rut):
    pass


# FUNCION 5: AGREGAR O QUITAR DEPOSITO AL USUARIO
# Dado un rut, un monto y una transacción que puede ser un deposito o un retiro
# Debes añadir la transacción a la cuenta del cliente, siguiendo las restricciones:
# - El cliente debe existir en el banco.
# - El tipo de transacción debe ser o "deposito" o "retiro"
# - El monto a agregar debe ser un numero entero y positivo mayor a 0.
# - Si la transacción es un retiro, debes verificar que el usuario tiene suficiente saldo en la cuenta.
# - En caso de no cumplir alguna de estas reglas, debes avisar cuál fue el problema.
def nueva_transaccion(historial, rut, monto, transaccion="deposito"):
    pass


# FUNCION 6: CREAR MENÚ DE INTERACCIÓN
# Debes crear un menú con el que se pueda interactuar con tu programa. Para esto debes:
# - Imprimir un listado de las posibles opciones de tu menú, incluyendo una para terminar el programa.
# - Permitir que el usuario ingrese una opción mediante la terminal.
# - Si la opcion es válida (una de las posibles), pedir los argumentos faltantes por consola y ejecutarla.
# - Si la opción no está en el listado posible, avisar al usuario.
# - El menú debe funcionar de manera infinita (es decir, volver a pedir opciones luego de ejecutar
#   una acción) hasta que se seleccione la opción de terminar el programa. En ese caso, la función debe finalizar.
def programa_interactivo(historial):
    pass


# ESTA SECCIÓN TE PERMITE PROBAR TU CÓDIGO
if __name__ == "__main__":
    # CAMBIAR ENTRE TRUE Y FALSE SI DESEAS PROBARLO DE FORMA INTERACTIVA MEDIANTE
    INTERACTIVO = False

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
