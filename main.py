################################################################################
################################ MINIPROYECTO 2 ################################
################################################################################

# Instrucciones: A continuación se presentan X funciones, las cuáles están vacías o incompletas.
# Tu trabajo es completarlas según las especificaciones del enunciado.
# Podrás probar tus funciones modificando la sección final del código y ejecutando
# este programa mediante el comando "python3 main.py"

# PARTE 1:
# Añade en esta sección todos los imports que consideres necesarios

import os


# PARTE 2:
# Completa las siguientes funciones.

# FUNCIÓN 1: CARGAR DATOS A PARTIR DE UN CSV
# Deberás recibir el nombre de un archivo CSV (el cual ya incluye la extensión) y retornar
# Un dataframe con los datos cargados.
def cargar_datos(archivo):
    pass


# FUNCIÓN 2: LIMPIAR DATOS DE INCIDENTES
# La base de datos de incidentes está corrupta. Deberás limpiar el dataframe, eliminando
# las filas que cumplan las siguientes condiciones:
# 1. Filas cuya columna incident_id no sea válida (tenga un "-")
# 2. Filas cuya columna month no sea válida (valores mayores a 12)
# 3. Filas cuya columna is_fatal no sea válida (valores que no sean ni 1 ni 0)
# Deberás retornar el dataframe final.
def limpiar_incidentes(dataframe_incidentes):
    pass


# FUNCIÓN 3: OBTENER CONSULTA 1
# Mediante funciones vistas esta semana, debes poder resolver la siguiente pregunta:
# ¿Cuantos pasajeros anuales tienen en promedio las aerolineas? ¿Cuántos años llevan operando en promedio?
def obtener_consulta_1(dataframe_aerolineas):
    # Realiza tu desarrollo de código aquí
    print("Completa este print con tu respuesta de la consulta 1.")


# FUNCIÓN 4: OBTENER CONSULTA 2
# Mediante funciones vistas esta semana, debes poder resolver la siguiente pregunta:
# ¿Cuáles son las 5 causas más comunes de los incidentes en aviones?
def obtener_consulta_2(dataframe_incidentes):
    # Realiza tu desarrollo de código aquí
    print("Completa este print con tu respuesta de la consulta 2.")


# FUNCION 5: OBTENER CONSULTA 3
# Mediante funciones vistas esta semana, debes poder resolver la siguiente pregunta:
# ¿Cuál es el manufacturador con menos incidentes? ¿Cuántos de estos incidentes fueron fatales?
def obtener_consulta_3(dataframe_incidentes):
    # Realiza tu desarrollo de código aquí
    print("Completa este print con tu respuesta de la consulta 3.")


# FUNCIÓN 6: OBTENER CONSULTA 4
# Mediante funciones vistas esta semana, debes poder resolver la siguiente pregunta:
# ¿Cuál es la región con más incidentes? ¿Cuál es la región con menos incidentes?
def obtener_consulta_4(dataframe_incidentes, dataframe_aerolineas):
    # Realiza tu desarrollo de código aquí
    print("Completa este print con tu respuesta de la consulta 4.")


# FUNCIÓN 7: OBTENER CONSULTA 5
# Mediante funciones vistas esta semana, debes poder resolver la siguiente pregunta:
# Considerando solo los incidentes no fatales, ¿Cuántos incidentes en promedio tienen una aerolínea
# de América del norte? ¿Cuál es el tipo de incidente más común de este continente?
def obtener_consulta_5(dataframe_incidentes, dataframe_aerolineas):
    # Realiza tu desarrollo de código aquí
    print("Completa este print con tu respuesta de la consulta 5.")

# ESTA SECCION EJECUTA TU CÓDIGO PRINCIPAL
# NO MODIFICAR
if __name__ == "__main__":
    # CARGAR DATOS
    aerolineas = cargar_datos(os.path.join("data", "aerolineas.csv"))
    incidentes_corruptos = cargar_datos(os.path.join("data", "incidentes.csv"))

    # LIMPIAR INCIDENTES CORRUPTOS
    incidentes = limpiar_incidentes(incidentes_corruptos)

    # CONSULTAS DE 1 TABLA
    obtener_consulta_1(aerolineas)
    obtener_consulta_2(incidentes)
    obtener_consulta_3(incidentes)

    # CONSULTAS DE 2 TABLAS
    obtener_consulta_4(incidentes, aerolineas)
    obtener_consulta_5(incidentes, aerolineas)
