# utils.py
# Módulo de utilidades y validación de datos.
# Contiene funciones auxiliares que se reutilizan en otros módulos del proyecto.
# Aquí se valida que los datos de cada estudiante sean correctos
# y se ofrecen herramientas para limpiar texto.

import re  # librería de expresiones regulares (módulo 7)


def validar_estudiante(estudiante):
    """
    Valida que un diccionario de estudiante tenga datos correctos.
    Recibe un diccionario con las llaves: nombre, carrera, edad, promedio.
    Retorna True si todo es válido, False si algo está mal.
    """

    # Verificar que el nombre no esté vacío (después de quitar espacios en blanco)
    # strip() elimina espacios al inicio y al final del texto
    if not estudiante.get("nombre", "").strip():
        return False

    # Verificar que la carrera no esté vacía
    if not estudiante.get("carrera", "").strip():
        return False

    # Verificar que la edad sea un número entero positivo
    edad = estudiante.get("edad", None)
    if not isinstance(edad, int) or edad <= 0:
        return False

    # Verificar que el promedio sea un número entre 0 y 10
    promedio = estudiante.get("promedio", None)
    if not isinstance(promedio, (int, float)) or promedio < 0 or promedio > 10:
        return False

    # Si pasó todas las verificaciones, el estudiante es válido
    return True


def limpiar_texto(texto):
    """
    Limpia un texto eliminando espacios extra al inicio, al final,
    y espacios dobles en el medio.
    Usa expresiones regulares (módulo 7).
    Ejemplo: "  Ana   María  " se convierte en "Ana María"
    """

    # strip() quita espacios al inicio y final
    texto = texto.strip()

    # re.sub() reemplaza un patrón por otra cosa
    # r"\s+" significa "uno o más espacios en blanco"
    # Lo reemplazamos por un solo espacio " "
    texto = re.sub(r"\s+", " ", texto)

    return texto


def mostrar_estudiantes(estudiantes):
    """
    Muestra una lista de estudiantes en formato legible en la terminal.
    Recibe una lista de diccionarios (cada diccionario es un estudiante).
    No retorna nada, solo imprime en pantalla.
    """

    # Si la lista está vacía, avisar al usuario
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return

    # Imprimir una cabecera para que se vea ordenado
    # f-string con formato: {valor:<15} significa "ocupa 15 espacios, alineado a la izquierda"
    print(f"{'Nombre':<15} {'Carrera':<15} {'Edad':<6} {'Promedio':<8}")
    print("-" * 46)  # línea separadora de 46 guiones

    # Recorrer cada estudiante e imprimir sus datos
    for est in estudiantes:
        print(f"{est['nombre']:<15} {est['carrera']:<15} {est['edad']:<6} {est['promedio']:<8}")