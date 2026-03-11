# data_loader.py
# Módulo encargado de cargar (leer) los datos desde un archivo CSV.
# Lee el archivo, convierte los datos al tipo correcto (texto, entero, decimal)
# y valida cada estudiante antes de agregarlo a la lista final.

import csv  # librería para leer archivos CSV (módulo 6)
from utils import validar_estudiante, limpiar_texto  # importamos funciones de utils.py (módulo 4)


def cargar_datos(ruta_archivo):
    """
    Lee un archivo CSV y retorna una lista de diccionarios.
    Cada diccionario representa un estudiante con sus datos.
    Si el archivo no existe o tiene datos mal formateados, maneja el error
    sin que el programa se rompa.

    Parámetro:
        ruta_archivo: texto con la ruta del archivo CSV (ejemplo: "data/estudiantes.csv")

    Retorna:
        Una lista de diccionarios con los estudiantes válidos.
        Si hay error, retorna una lista vacía.
    """

    # Lista donde se guardarán los estudiantes válidos
    estudiantes = []

    # try/except para manejar errores sin que el programa se rompa (módulo 3)
    try:
        # Abrir el archivo usando "with" para que se cierre automáticamente (módulo 6)
        # encoding="utf-8" permite leer caracteres especiales como tildes (á, é, í, ó, ú)
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            # csv.DictReader lee el CSV y convierte cada fila en un diccionario
            # usando la primera línea (cabecera) como llaves (módulo 6)
            lector = csv.DictReader(archivo)

            # Recorrer cada fila del archivo (cada fila es un estudiante)
            for fila in lector:

                # try/except interno para manejar errores en filas individuales
                # Si una fila tiene un dato mal formateado, la saltamos
                # pero seguimos leyendo las demás (módulo 3)
                try:
                    # Crear el diccionario del estudiante
                    # limpiar_texto() limpia espacios extra en nombre y carrera
                    # int() convierte el texto de edad a número entero
                    # float() convierte el texto de promedio a número decimal
                    estudiante = {
                        "nombre": limpiar_texto(fila["nombre"]),
                        "carrera": limpiar_texto(fila["carrera"]),
                        "edad": int(fila["edad"]),
                        "promedio": float(fila["promedio"])
                    }

                    # Validar que los datos del estudiante sean correctos
                    # Si es válido, lo agregamos a la lista
                    if validar_estudiante(estudiante):
                        estudiantes.append(estudiante)
                    else:
                        # Si no es válido, avisamos cuál fila tiene problemas
                        print(f"Advertencia: datos inválidos en fila: {fila}")

                # ValueError ocurre cuando int() o float() reciben texto que no es número
                # Ejemplo: int("abc") lanza ValueError
                except ValueError:
                    print(f"Advertencia: error al convertir datos en fila: {fila}")

    # FileNotFoundError ocurre cuando el archivo no existe en la ruta indicada
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_archivo}'")

    # Retornar la lista de estudiantes (puede estar vacía si hubo errores)
    return estudiantes