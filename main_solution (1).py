################################################################################
############ EJERCICIO DE PRÁCTICA — CATÁLOGO DE LIBRERÍA — SOLUCIÓN (TA) ####
################################################################################
import pprint
import practica_utilidades as utilidades


def crear_catalogo(nombre):
    libros_sin_procesar = utilidades.cargar_csv(nombre)

    catalogo = {}
    for linea in libros_sin_procesar[1:]:
        isbn, titulo, autor, genero, stock = linea.split(",")
        catalogo[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "stock": int(stock),
        }

    return catalogo


def listar_por_genero(catalogo, genero):
    titulos = []
    for info in catalogo.values():
        if info["genero"] == genero:
            titulos.append(info["titulo"])
    return titulos


def registrar_libro(catalogo, isbn, titulo, autor, genero, stock_inicial):
    if isbn in catalogo:
        print("El libro ya existe en el catálogo.")
        return

    catalogo[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "stock": stock_inicial,
    }
    print(f"Registrado el libro {titulo}")


def buscar_libro(catalogo, isbn):
    if isbn not in catalogo:
        print(f"El libro con isbn {isbn} no existe en el catálogo.")
        return

    libro = catalogo[isbn]
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Género: {libro['genero']}")
    print(f"Stock disponible: {libro['stock']} unidades.")


def actualizar_stock(catalogo, isbn, cantidad, operacion="agregar"):
    if isbn not in catalogo:
        print(f"El libro con isbn {isbn} no existe en el catálogo.")
        return

    if operacion not in ("agregar", "quitar"):
        print(f"La operación {operacion} no está en las permitidas.")
        return

    if not isinstance(cantidad, int) or isinstance(cantidad, bool):
        print("La cantidad no es un int, sino un float.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    if operacion == "quitar":
        if catalogo[isbn]["stock"] < cantidad:
            print("El libro no tiene stock suficiente para esa operación.")
            return
        catalogo[isbn]["stock"] -= cantidad
    else:  # agregar
        catalogo[isbn]["stock"] += cantidad

    print("El stock fue actualizado correctamente.")


def agrupar_por_autor(catalogo):
    por_autor = {}
    for info in catalogo.values():
        autor = info["autor"]
        if autor not in por_autor:
            por_autor[autor] = []
        por_autor[autor].append(info["titulo"])
    return por_autor


def programa_interactivo(catalogo):
    opciones = {
        "1": "Listar títulos de un género",
        "2": "Registrar un nuevo libro",
        "3": "Buscar la ficha de un libro",
        "4": "Actualizar stock de un libro",
        "5": "Agrupar títulos por autor",
        "-1": "Salir del programa",
    }

    while True:
        print("\nBienvenido al catálogo. ¿Cuál es la acción que deseas realizar?")
        for clave, texto in opciones.items():
            print(f" [{clave}] {texto}")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            genero = input("Ingrese el género a buscar: ").strip()
            print(listar_por_genero(catalogo, genero))
        elif opcion == "2":
            isbn = input("Ingrese el ISBN: ").strip()
            titulo = input("Ingrese el título: ").strip()
            autor = input("Ingrese el autor: ").strip()
            genero = input("Ingrese el género: ").strip()
            stock_inicial = int(input("Ingrese el stock inicial: ").strip())
            registrar_libro(catalogo, isbn, titulo, autor, genero, stock_inicial)
        elif opcion == "3":
            isbn = input("Ingrese el ISBN: ").strip()
            buscar_libro(catalogo, isbn)
        elif opcion == "4":
            isbn = input("Ingrese el ISBN: ").strip()
            cantidad = input("Ingrese la cantidad: ").strip()
            cantidad = int(cantidad) if cantidad.lstrip("-").isdigit() else float(cantidad)
            operacion = input("Ingrese la operación (agregar/quitar): ").strip()
            actualizar_stock(catalogo, isbn, cantidad, operacion)
        elif opcion == "5":
            pprint.pp(agrupar_por_autor(catalogo))
        elif opcion == "-1":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    INTERACTIVO = False

    catalogo_libreria = crear_catalogo("catalogo.csv")
    if catalogo_libreria:
        if INTERACTIVO:
            programa_interactivo(catalogo_libreria)
        else:
            print("\nCatálogo cargado. Mostrando información de un libro:")
            pprint.pp(catalogo_libreria["978-84-204-8188-9"])
            print("\nMostrando títulos del género 'Cuento'")
            print(listar_por_genero(catalogo_libreria, "Cuento"))
            print("\nRegistrando un libro nuevo")
            print(registrar_libro(catalogo_libreria, "978-0-00-000000-0", "Kafka en la orilla", "Haruki Murakami", "Novela", 5))
            print("\nBuscando la ficha de algunos libros...")
            buscar_libro(catalogo_libreria, "978-0-00-000000-0")
            buscar_libro(catalogo_libreria, "978-84-9838-536-7")
            buscar_libro(catalogo_libreria, "000-0-00-000000-0")
            print("\nActualizando stock")
            actualizar_stock(catalogo_libreria, "000-0-00-000000-0", 3, "agregar")
            actualizar_stock(catalogo_libreria, "978-956-315-057-4", 2, "quitar")
            actualizar_stock(catalogo_libreria, "978-84-204-8188-9", 1.5, "quitar")
            actualizar_stock(catalogo_libreria, "978-84-204-8188-9", 3, "quitar")
            actualizar_stock(catalogo_libreria, "978-84-204-8188-9", 10, "agregar")
            actualizar_stock(catalogo_libreria, "978-84-204-8188-9", 5, "quitar")
            print("\nAgrupando el catálogo por autor")
            pprint.pp(agrupar_por_autor(catalogo_libreria))
    else:
        print("Llena primero la función crear_catalogo antes de probar tu código.")