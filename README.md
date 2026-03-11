# DataManager CLI — Sistema de Gestión y Análisis de Datos

Proyecto integrador del curso **Introducción a la Programación en Python y Pytorch**
Maestría en Estadística, FIEECS-UNI

**Fecha:** 13 de marzo de 2026

## Programadores

* Torres Padilla Erik Washington

## Descripción

DataManager CLI es una aplicación de línea de comandos que permite gestionar registros académicos de estudiantes. El programa permite cargar datos desde archivos CSV, validarlos, filtrarlos, ordenarlos, calcular estadísticas básicas y exportar los resultados en formato JSON.

## Estructura del Proyecto

```
datamanager/
│
├── main.py              # Módulo principal con el menú interactivo (CLI)
├── data_loader.py       # Módulo para cargar y leer datos desde archivos CSV
├── processor.py         # Módulo de procesamiento: filtros, ordenamiento, estadísticas
├── exporter.py          # Módulo para exportar resultados a archivos JSON
├── utils.py             # Módulo de utilidades: validación y limpieza de datos
│
├── tests/
│   ├── __init__.py      # Indica que "tests" es un paquete de Python
│   └── test_processor.py  # Pruebas unitarias para processor.py (24 tests)
│
└── data/
    └── estudiantes.csv  # Archivo de datos de ejemplo
```

## Requisitos

- Python 3.10 o superior
- pytest (para ejecutar las pruebas unitarias)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/usuario/datamanager.git
cd datamanager
```

2. Instalar dependencias:
```bash
pip install pytest
```

## Ejecución

Desde la carpeta `datamanager`, ejecutar:

```bash
python main.py
```

Aparecerá el menú principal:

```
========================================
   DataManager CLI - Menú Principal
========================================
1 - Cargar datos
2 - Filtrar
3 - Ordenar
4 - Mostrar estadísticas
5 - Exportar resultados
6 - Salir
========================================
```

## Ejemplo de Uso

### 1. Cargar datos
```
Seleccione una opción: 1
Ingrese la ruta del archivo CSV: data/estudiantes.csv

Se cargaron 10 estudiantes exitosamente.
Nombre          Carrera         Edad   Promedio
----------------------------------------------
Ana             Ingeniería      21     8.5
Luis            Matemática      22     7.8
Carla           Física          20     9.1
...
```

### 2. Filtrar por promedio
```
Seleccione una opción: 2

--- Opciones de filtrado ---
1 - Filtrar por promedio mínimo
2 - Filtrar por carrera
3 - Filtrar por edad mínima
Seleccione una opción: 1
Ingrese el promedio mínimo: 8.5

Estudiantes con promedio >= 8.5:
Nombre          Carrera         Edad   Promedio
----------------------------------------------
Ana             Ingeniería      21     8.5
Carla           Física          20     9.1
María           Estadística     21     9.4
Sofía           Matemática      20     8.8
Valentina       Ingeniería      21     9.0
```

### 3. Ordenar por promedio
```
Seleccione una opción: 3

--- Opciones de ordenamiento ---
1 - Ordenar por nombre
2 - Ordenar por promedio
3 - Ordenar por edad
Seleccione una opción: 2
¿Orden descendente? (s/n): s

Estudiantes ordenados por promedio:
Nombre          Carrera         Edad   Promedio
----------------------------------------------
María           Estadística     21     9.4
Carla           Física          20     9.1
Valentina       Ingeniería      21     9.0
...
```

### 4. Mostrar estadísticas
```
Seleccione una opción: 4

--- Estadísticas Generales ---
Total de estudiantes: 10
Promedio general: 7.9
Edad máxima: 24
Edad mínima: 20
Conteo por carrera:
  Ingeniería: 3
  Matemática: 2
  Física: 3
  Estadística: 2
```

### 5. Exportar resultados
```
Seleccione una opción: 5

--- Opciones de exportación ---
1 - Exportar estadísticas
2 - Exportar lista de estudiantes (actual/ordenada)
3 - Exportar último filtro aplicado
Seleccione una opción: 1
Ingrese la ruta para guardar el JSON: data/estadisticas.json

Resultados exportados exitosamente en 'data/estadisticas.json'
```

Ejemplo de archivo JSON exportado (`data/estadisticas.json`):
```json
{
  "total_estudiantes": 10,
  "promedio_general": 7.9,
  "edad_maxima": 24,
  "edad_minima": 20,
  "conteo_por_carrera": {
    "Ingeniería": 3,
    "Matemática": 2,
    "Física": 3,
    "Estadística": 2
  }
}
```

## Ejecución de Pruebas

Para ejecutar las 24 pruebas unitarias:

```bash
pytest tests/test_processor.py -v
```

Resultado esperado:
```
tests/test_processor.py::test_filtrar_por_promedio_valores_normales PASSED
tests/test_processor.py::test_filtrar_por_promedio_ninguno_cumple PASSED
tests/test_processor.py::test_filtrar_por_promedio_todos_cumplen PASSED
...
====== 24 passed ======
```

## Formato del Archivo CSV

El archivo CSV debe tener la siguiente estructura:

```
nombre,carrera,edad,promedio
Ana,Ingeniería,21,8.5
Luis,Matemática,22,7.8
```

- **nombre**: texto (no vacío)
- **carrera**: texto (no vacío)
- **edad**: número entero positivo
- **promedio**: número decimal entre 0 y 10

## Módulos del Curso Integrados

| Módulo | Tema | Aplicación en el Proyecto |
|--------|------|--------------------------|
| 1 | Introducción a Python | Funciones, main(), f-strings, input/output |
| 2 | Control de Flujo | Condicionales, bucles, listas, diccionarios |
| 3 | Manejo de Errores | try/except, validación robusta, CLI robusta |
| 4 | Librerías y Módulos | Organización modular, JSON, imports propios |
| 5 | Testing | Pruebas unitarias con pytest y assert |
| 6 | Entrada/Salida | Lectura CSV, escritura JSON, uso de with |
| 7 | Expresiones Regulares | Limpieza de texto con re.sub() |

