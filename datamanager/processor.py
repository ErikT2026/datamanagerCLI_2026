# processor.py
# Módulo de procesamiento de datos.
# Contiene las funciones que filtran, ordenan y calculan estadísticas
# sobre la lista de estudiantes.
# Estas funciones NO piden datos al usuario ni imprimen en pantalla.
# Solo reciben datos, los procesan y retornan resultados.
# Eso las hace "testeables" (se pueden probar automáticamente con pytest).


def filtrar_por_promedio(estudiantes, promedio_minimo):
    """
    Filtra estudiantes cuyo promedio sea mayor o igual al valor indicado.

    Parámetros:
        estudiantes: lista de diccionarios (cada uno es un estudiante)
        promedio_minimo: número decimal, el promedio mínimo para pasar el filtro

    Retorna:
        Una nueva lista solo con los estudiantes que cumplen el criterio.
    """

    # Lista donde se guardarán los que cumplan el filtro
    filtrados = []

    # Recorrer cada estudiante y verificar su promedio (módulo 2: bucles y condicionales)
    for est in estudiantes:
        if est["promedio"] >= promedio_minimo:
            filtrados.append(est)

    return filtrados


def filtrar_por_carrera(estudiantes, carrera):
    """
    Filtra estudiantes que pertenezcan a una carrera específica.
    La comparación ignora mayúsculas/minúsculas para que
    "física", "Física" y "FÍSICA" sean lo mismo.

    Parámetros:
        estudiantes: lista de diccionarios
        carrera: texto con el nombre de la carrera a buscar

    Retorna:
        Una nueva lista solo con los estudiantes de esa carrera.
    """

    filtrados = []

    # lower() convierte el texto a minúsculas para comparar sin importar mayúsculas
    for est in estudiantes:
        if est["carrera"].lower() == carrera.lower():
            filtrados.append(est)

    return filtrados


def filtrar_por_edad_minima(estudiantes, edad_minima):
    """
    Filtra estudiantes cuya edad sea mayor o igual a la edad indicada.

    Parámetros:
        estudiantes: lista de diccionarios
        edad_minima: número entero, la edad mínima para pasar el filtro

    Retorna:
        Una nueva lista solo con los estudiantes que cumplen el criterio.
    """

    filtrados = []

    for est in estudiantes:
        if est["edad"] >= edad_minima:
            filtrados.append(est)

    return filtrados


def ordenar_estudiantes(estudiantes, campo, descendente=False):
    """
    Ordena la lista de estudiantes según un campo específico.
    Usa sorted() con key=lambda, tal como se vio en clase (módulo 6).

    Parámetros:
        estudiantes: lista de diccionarios
        campo: texto que indica por cuál dato ordenar ("nombre", "carrera", "edad" o "promedio")
        descendente: True para ordenar de mayor a menor, False para menor a mayor
                     (por defecto es False, o sea de menor a mayor)

    Retorna:
        Una nueva lista ordenada según el criterio indicado.
    """

    # sorted() crea una nueva lista ordenada sin modificar la original
    # key=lambda est: est[campo] le dice a sorted() "usa este dato para comparar"
    # reverse=descendente le dice si va de mayor a menor (True) o menor a mayor (False)
    return sorted(estudiantes, key=lambda est: est[campo], reverse=descendente)


def calcular_promedio_general(estudiantes):
    """
    Calcula el promedio general de todos los estudiantes.

    Parámetro:
        estudiantes: lista de diccionarios

    Retorna:
        Un número decimal con el promedio general.
        Si la lista está vacía, retorna 0.
    """

    # Si la lista está vacía, retornar 0 para evitar dividir entre cero
    if not estudiantes:
        return 0

    # Sumar todos los promedios
    suma = 0
    for est in estudiantes:
        suma += est["promedio"]

    # Dividir la suma entre la cantidad de estudiantes
    # round(..., 2) redondea a 2 decimales
    return round(suma / len(estudiantes), 2)


def obtener_edad_maxima(estudiantes):
    """
    Encuentra la edad más alta entre todos los estudiantes.

    Retorna:
        Un número entero con la edad máxima.
        Si la lista está vacía, retorna 0.
    """

    if not estudiantes:
        return 0

    # Empezamos asumiendo que el primero tiene la edad más alta
    maxima = estudiantes[0]["edad"]

    # Comparamos con cada uno de los demás
    for est in estudiantes:
        if est["edad"] > maxima:
            maxima = est["edad"]

    return maxima


def obtener_edad_minima(estudiantes):
    """
    Encuentra la edad más baja entre todos los estudiantes.

    Retorna:
        Un número entero con la edad mínima.
        Si la lista está vacía, retorna 0.
    """

    if not estudiantes:
        return 0

    # Empezamos asumiendo que el primero tiene la edad más baja
    minima = estudiantes[0]["edad"]

    # Comparamos con cada uno de los demás
    for est in estudiantes:
        if est["edad"] < minima:
            minima = est["edad"]

    return minima


def contar_por_carrera(estudiantes):
    """
    Cuenta cuántos estudiantes hay en cada carrera.

    Retorna:
        Un diccionario donde las llaves son las carreras
        y los valores son la cantidad de estudiantes.
        Ejemplo: {"Ingeniería": 3, "Física": 2, "Matemática": 2}
    """

    # Diccionario vacío donde se irá acumulando el conteo
    conteo = {}

    for est in estudiantes:
        carrera = est["carrera"]

        # Si la carrera ya está en el diccionario, sumar 1
        # Si no está, agregarla con valor 1
        if carrera in conteo:
            conteo[carrera] += 1
        else:
            conteo[carrera] = 1

    return conteo


def generar_estadisticas(estudiantes):
    """
    Genera un resumen completo con todas las estadísticas.
    Este es el diccionario que luego se exportará a JSON.

    Retorna:
        Un diccionario con el resumen estadístico.
    """

    return {
        "total_estudiantes": len(estudiantes),
        "promedio_general": calcular_promedio_general(estudiantes),
        "edad_maxima": obtener_edad_maxima(estudiantes),
        "edad_minima": obtener_edad_minima(estudiantes),
        "conteo_por_carrera": contar_por_carrera(estudiantes)
    }