# test_processor.py
# Módulo de pruebas unitarias (unit tests) para processor.py
# Usa pytest para verificar que cada función del procesador funcione correctamente.
# Se prueban casos normales, casos extremos (lista vacía) y casos límite.
# Las funciones de test deben empezar con "test_" para que pytest las detecte.

import pytest  # librería de testing automatizado (módulo 5)

# Importar las funciones que vamos a probar
# Como este archivo está dentro de la carpeta "tests/",
# importamos desde el módulo processor que está un nivel arriba
from processor import (
    filtrar_por_promedio,
    filtrar_por_carrera,
    filtrar_por_edad_minima,
    ordenar_estudiantes,
    calcular_promedio_general,
    obtener_edad_maxima,
    obtener_edad_minima,
    contar_por_carrera,
    generar_estadisticas
)


# === Datos de prueba ===
# Creamos una lista de estudiantes "falsa" para usar en todos los tests.
# Así no dependemos del archivo CSV real (módulo 5: funciones testeables).
estudiantes_prueba = [
    {"nombre": "Ana", "carrera": "Ingeniería", "edad": 21, "promedio": 8.5},
    {"nombre": "Luis", "carrera": "Matemática", "edad": 22, "promedio": 7.8},
    {"nombre": "Carla", "carrera": "Física", "edad": 20, "promedio": 9.1},
    {"nombre": "Pedro", "carrera": "Ingeniería", "edad": 23, "promedio": 6.5},
    {"nombre": "María", "carrera": "Estadística", "edad": 21, "promedio": 9.4},
]


# =============================================
# Tests para filtrar_por_promedio
# =============================================

def test_filtrar_por_promedio_valores_normales():
    """Verifica que filtre correctamente con un promedio mínimo normal."""
    # Solo Ana (8.5), Carla (9.1) y María (9.4) tienen promedio >= 8.5
    resultado = filtrar_por_promedio(estudiantes_prueba, 8.5)
    assert len(resultado) == 3


def test_filtrar_por_promedio_ninguno_cumple():
    """Verifica que retorne lista vacía si nadie cumple el filtro."""
    # Nadie tiene promedio >= 10
    resultado = filtrar_por_promedio(estudiantes_prueba, 10)
    assert len(resultado) == 0


def test_filtrar_por_promedio_todos_cumplen():
    """Verifica que retorne todos si el mínimo es muy bajo."""
    # Todos tienen promedio >= 0
    resultado = filtrar_por_promedio(estudiantes_prueba, 0)
    assert len(resultado) == 5


def test_filtrar_por_promedio_lista_vacia():
    """Verifica que funcione con lista vacía sin romperse."""
    resultado = filtrar_por_promedio([], 8.0)
    assert resultado == []


# =============================================
# Tests para filtrar_por_carrera
# =============================================

def test_filtrar_por_carrera_existente():
    """Verifica que filtre correctamente una carrera que existe."""
    # Ana y Pedro son de Ingeniería
    resultado = filtrar_por_carrera(estudiantes_prueba, "Ingeniería")
    assert len(resultado) == 2


def test_filtrar_por_carrera_no_existente():
    """Verifica que retorne lista vacía si la carrera no existe."""
    resultado = filtrar_por_carrera(estudiantes_prueba, "Medicina")
    assert len(resultado) == 0


def test_filtrar_por_carrera_ignora_mayusculas():
    """Verifica que la comparación ignore mayúsculas/minúsculas."""
    # "física" en minúsculas debería encontrar "Física"
    resultado = filtrar_por_carrera(estudiantes_prueba, "física")
    assert len(resultado) == 1


def test_filtrar_por_carrera_lista_vacia():
    """Verifica que funcione con lista vacía sin romperse."""
    resultado = filtrar_por_carrera([], "Ingeniería")
    assert resultado == []


# =============================================
# Tests para filtrar_por_edad_minima
# =============================================

def test_filtrar_por_edad_minima_valores_normales():
    """Verifica que filtre correctamente por edad mínima."""
    # Luis (22) y Pedro (23) tienen edad >= 22
    resultado = filtrar_por_edad_minima(estudiantes_prueba, 22)
    assert len(resultado) == 2


def test_filtrar_por_edad_minima_lista_vacia():
    """Verifica que funcione con lista vacía sin romperse."""
    resultado = filtrar_por_edad_minima([], 20)
    assert resultado == []


# =============================================
# Tests para ordenar_estudiantes
# =============================================

def test_ordenar_por_nombre_ascendente():
    """Verifica que ordene por nombre de A a Z."""
    resultado = ordenar_estudiantes(estudiantes_prueba, "nombre")
    # El primer nombre alfabéticamente es "Ana"
    assert resultado[0]["nombre"] == "Ana"
    # El último es "Pedro"
    assert resultado[-1]["nombre"] == "Pedro"


def test_ordenar_por_promedio_descendente():
    """Verifica que ordene por promedio de mayor a menor."""
    resultado = ordenar_estudiantes(estudiantes_prueba, "promedio", descendente=True)
    # María tiene el promedio más alto (9.4)
    assert resultado[0]["nombre"] == "María"
    # Pedro tiene el más bajo (6.5)
    assert resultado[-1]["nombre"] == "Pedro"


def test_ordenar_lista_vacia():
    """Verifica que ordenar una lista vacía no cause error."""
    resultado = ordenar_estudiantes([], "nombre")
    assert resultado == []


# =============================================
# Tests para calcular_promedio_general
# =============================================

def test_calcular_promedio_general_valores_normales():
    """Verifica el cálculo del promedio con valores normales."""
    # (8.5 + 7.8 + 9.1 + 6.5 + 9.4) / 5 = 41.3 / 5 = 8.26
    resultado = calcular_promedio_general(estudiantes_prueba)
    assert resultado == 8.26


def test_calcular_promedio_general_lista_vacia():
    """Verifica que retorne 0 con lista vacía (evitar dividir entre cero)."""
    resultado = calcular_promedio_general([])
    assert resultado == 0


def test_calcular_promedio_general_un_estudiante():
    """Verifica el cálculo con un solo estudiante."""
    un_estudiante = [{"nombre": "Ana", "carrera": "Ingeniería", "edad": 21, "promedio": 8.5}]
    resultado = calcular_promedio_general(un_estudiante)
    assert resultado == 8.5


# =============================================
# Tests para obtener_edad_maxima y obtener_edad_minima
# =============================================

def test_obtener_edad_maxima_valores_normales():
    """Verifica que encuentre la edad más alta."""
    # Pedro tiene 23, que es la mayor edad
    resultado = obtener_edad_maxima(estudiantes_prueba)
    assert resultado == 23


def test_obtener_edad_maxima_lista_vacia():
    """Verifica que retorne 0 con lista vacía."""
    resultado = obtener_edad_maxima([])
    assert resultado == 0


def test_obtener_edad_minima_valores_normales():
    """Verifica que encuentre la edad más baja."""
    # Carla tiene 20, que es la menor edad
    resultado = obtener_edad_minima(estudiantes_prueba)
    assert resultado == 20


def test_obtener_edad_minima_lista_vacia():
    """Verifica que retorne 0 con lista vacía."""
    resultado = obtener_edad_minima([])
    assert resultado == 0


# =============================================
# Tests para contar_por_carrera
# =============================================

def test_contar_por_carrera_valores_normales():
    """Verifica que cuente correctamente cada carrera."""
    resultado = contar_por_carrera(estudiantes_prueba)
    assert resultado["Ingeniería"] == 2
    assert resultado["Matemática"] == 1
    assert resultado["Física"] == 1
    assert resultado["Estadística"] == 1


def test_contar_por_carrera_lista_vacia():
    """Verifica que retorne diccionario vacío con lista vacía."""
    resultado = contar_por_carrera([])
    assert resultado == {}


# =============================================
# Tests para generar_estadisticas
# =============================================

def test_generar_estadisticas_completas():
    """Verifica que el resumen estadístico contenga todas las llaves correctas."""
    resultado = generar_estadisticas(estudiantes_prueba)
    # Verificar que el diccionario tenga todas las llaves esperadas
    assert resultado["total_estudiantes"] == 5
    assert resultado["promedio_general"] == 8.26
    assert resultado["edad_maxima"] == 23
    assert resultado["edad_minima"] == 20
    assert "conteo_por_carrera" in resultado


def test_generar_estadisticas_lista_vacia():
    """Verifica que funcione con lista vacía sin romperse."""
    resultado = generar_estadisticas([])
    assert resultado["total_estudiantes"] == 0
    assert resultado["promedio_general"] == 0