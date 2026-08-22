"""
Utilidades para el MP1
"""


def cargar_csv(name):
    """
     Lee el contenido de un archivo CSV
    """
    with open(name, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f.readlines()]
