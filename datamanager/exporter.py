# exporter.py
# Módulo encargado de exportar (guardar) resultados en un archivo JSON.
# JSON es un formato estándar para guardar datos estructurados
# que cualquier otro programa puede leer después.

import json  # librería para trabajar con formato JSON (módulo 4)


def exportar_json(datos, ruta_archivo):
    """
    Guarda un diccionario de datos en un archivo JSON.
    Se usa para exportar las estadísticas.

    Parámetros:
        datos: diccionario con la información a guardar
               (por ejemplo, las estadísticas generadas por processor.py)
        ruta_archivo: texto con la ruta donde se guardará el archivo
                      (ejemplo: "data/estadisticas.json")

    Retorna:
        True si se guardó correctamente, False si hubo un error.
    """

    # try/except para manejar errores al escribir el archivo (módulo 3)
    try:
        # Abrir el archivo en modo escritura ("w") usando "with" (módulo 6)
        # encoding="utf-8" permite guardar caracteres especiales como tildes
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:

            # json.dump() convierte el diccionario a formato JSON y lo escribe en el archivo
            # indent=2 hace que el archivo se vea ordenado con sangría de 2 espacios
            # ensure_ascii=False permite que las tildes se guarden correctamente
            #   (sin esto, "Física" se guardaría como "F\u00edsica")
            json.dump(datos, archivo, indent=2, ensure_ascii=False)

        print(f"Resultados exportados exitosamente en '{ruta_archivo}'")
        return True

    # Si la carpeta no existe o hay un problema al escribir
    except OSError as e:
        print(f"Error al exportar: {e}")
        return False


def exportar_estudiantes_json(estudiantes, ruta_archivo):
    """
    Guarda una lista de estudiantes en un archivo JSON.
    Se usa para exportar los resultados de filtrar u ordenar.

    Parámetros:
        estudiantes: lista de diccionarios (cada uno es un estudiante)
        ruta_archivo: texto con la ruta donde se guardará el archivo
                      (ejemplo: "data/filtrados.json")

    Retorna:
        True si se guardó correctamente, False si hubo un error.
    """

    # try/except para manejar errores al escribir el archivo (módulo 3)
    try:
        # Abrir el archivo en modo escritura ("w") usando "with" (módulo 6)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:

            # json.dump() también puede guardar listas, no solo diccionarios
            json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)

        print(f"Estudiantes exportados exitosamente en '{ruta_archivo}'")
        return True

    except OSError as e:
        print(f"Error al exportar: {e}")
        return False