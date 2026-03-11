# main.py
# Módulo principal del programa DataManager CLI.
# Este es el archivo que el usuario ejecuta para iniciar el programa.
# Contiene el menú interactivo y coordina las llamadas a los demás módulos.
# Es como el "director de orquesta" que conecta todas las piezas.

import sys  # módulo para funciones del sistema, como sys.exit() (módulo 4)

# Importar funciones de nuestros propios módulos (módulo 4)
# Esto es igual a como en clase se hacía: from saludos import hola, adios
from data_loader import cargar_datos
from processor import (
    filtrar_por_promedio,
    filtrar_por_carrera,
    filtrar_por_edad_minima,
    ordenar_estudiantes,
    generar_estadisticas
)
from exporter import exportar_json, exportar_estudiantes_json
from utils import mostrar_estudiantes


def mostrar_menu():
    """
    Imprime el menú principal en la terminal.
    No recibe ni retorna nada, solo imprime.
    """

    print("\n========================================")
    print("   DataManager CLI - Menú Principal")
    print("========================================")
    print("1 - Cargar datos")
    print("2 - Filtrar")
    print("3 - Ordenar")
    print("4 - Mostrar estadísticas")
    print("5 - Exportar resultados")
    print("6 - Salir")
    print("========================================")


def menu_filtrar(estudiantes):
    """
    Submenú para elegir qué tipo de filtro aplicar.
    Recibe la lista de estudiantes y retorna la lista filtrada.
    """

    print("\n--- Opciones de filtrado ---")
    print("1 - Filtrar por promedio mínimo")
    print("2 - Filtrar por carrera")
    print("3 - Filtrar por edad mínima")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        # try/except para validar que el usuario ingrese un número (módulo 3)
        try:
            valor = float(input("Ingrese el promedio mínimo (ejemplo: 8.0): ").strip())
            resultado = filtrar_por_promedio(estudiantes, valor)
            print(f"\nEstudiantes con promedio >= {valor}:")
            mostrar_estudiantes(resultado)
            return resultado
        except ValueError:
            print("Error: debe ingresar un número válido.")
            return []

    elif opcion == "2":
        carrera = input("Ingrese la carrera (ejemplo: Física): ").strip()

        # Validar que no esté vacío
        if not carrera:
            print("Error: debe ingresar el nombre de una carrera.")
            return []

        resultado = filtrar_por_carrera(estudiantes, carrera)
        print(f"\nEstudiantes de {carrera}:")
        mostrar_estudiantes(resultado)
        return resultado

    elif opcion == "3":
        try:
            valor = int(input("Ingrese la edad mínima (ejemplo: 22): ").strip())
            resultado = filtrar_por_edad_minima(estudiantes, valor)
            print(f"\nEstudiantes con edad >= {valor}:")
            mostrar_estudiantes(resultado)
            return resultado
        except ValueError:
            print("Error: debe ingresar un número entero válido.")
            return []

    else:
        print("Opción no válida.")
        return []


def menu_ordenar(estudiantes):
    """
    Submenú para elegir cómo ordenar los datos.
    Recibe la lista de estudiantes y retorna la lista ordenada.
    """

    print("\n--- Opciones de ordenamiento ---")
    print("1 - Ordenar por nombre")
    print("2 - Ordenar por promedio")
    print("3 - Ordenar por edad")

    opcion = input("Seleccione una opción: ").strip()

    # Determinar el campo según la opción elegida
    if opcion == "1":
        campo = "nombre"
    elif opcion == "2":
        campo = "promedio"
    elif opcion == "3":
        campo = "edad"
    else:
        print("Opción no válida.")
        return estudiantes

    # Preguntar si quiere orden ascendente o descendente
    direccion = input("¿Orden descendente? (s/n): ").strip().lower()
    descendente = (direccion == "s")

    resultado = ordenar_estudiantes(estudiantes, campo, descendente)
    print(f"\nEstudiantes ordenados por {campo}:")
    mostrar_estudiantes(resultado)
    return resultado


def menu_exportar(estudiantes, ultimo_filtro):
    """
    Submenú para elegir qué resultados exportar a JSON.
    Recibe la lista actual de estudiantes (puede estar ordenada)
    y el último resultado de filtrado.
    """

    print("\n--- Opciones de exportación ---")
    print("1 - Exportar estadísticas")
    print("2 - Exportar lista de estudiantes (actual/ordenada)")
    print("3 - Exportar último filtro aplicado")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        # Exportar estadísticas como diccionario
        stats = generar_estadisticas(estudiantes)
        ruta = input("Ingrese la ruta para guardar el JSON (ejemplo: data/estadisticas.json): ").strip()

        if not ruta:
            print("Error: debe ingresar una ruta de archivo.")
            return

        exportar_json(stats, ruta)

    elif opcion == "2":
        # Exportar la lista actual de estudiantes (puede estar ordenada)
        ruta = input("Ingrese la ruta para guardar el JSON (ejemplo: data/estudiantes_ordenados.json): ").strip()

        if not ruta:
            print("Error: debe ingresar una ruta de archivo.")
            return

        exportar_estudiantes_json(estudiantes, ruta)

    elif opcion == "3":
        # Exportar el último resultado de filtrado
        # Primero verificar que haya un filtro guardado
        if not ultimo_filtro:
            print("Error: no hay resultados de filtrado para exportar.")
            print("Primero use la opción 2 del menú principal para filtrar datos.")
            return

        ruta = input("Ingrese la ruta para guardar el JSON (ejemplo: data/filtrados.json): ").strip()

        if not ruta:
            print("Error: debe ingresar una ruta de archivo.")
            return

        exportar_estudiantes_json(ultimo_filtro, ruta)

    else:
        print("Opción no válida.")


def main():
    """
    Función principal del programa.
    Contiene el bucle while que mantiene el menú activo
    hasta que el usuario elija salir (módulo 3: interfaz CLI robusta).
    """

    # Variable donde se guardarán los estudiantes cargados
    # Empieza vacía porque aún no se ha cargado ningún archivo
    estudiantes = []

    # Variable donde se guardará el último resultado de filtrado
    # Se actualiza cada vez que el usuario usa la opción 2 (Filtrar)
    ultimo_filtro = []

    # Bucle principal: se repite hasta que el usuario elija "6 - Salir"
    # Esto es lo que el profesor pide: "uso de bucle while principal" (módulo 3)
    while True:

        # Mostrar el menú
        mostrar_menu()

        # Pedir al usuario que elija una opción
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # === OPCIÓN 1: Cargar datos ===
            ruta = input("Ingrese la ruta del archivo CSV (ejemplo: data/estudiantes.csv): ").strip()

            # Validar que no esté vacío
            if not ruta:
                print("Error: debe ingresar una ruta de archivo.")
                continue  # "continue" vuelve al inicio del while sin ejecutar lo de abajo

            estudiantes = cargar_datos(ruta)

            # Limpiar el último filtro porque se cargaron datos nuevos
            ultimo_filtro = []

            if estudiantes:
                print(f"\nSe cargaron {len(estudiantes)} estudiantes exitosamente.")
                mostrar_estudiantes(estudiantes)
            else:
                print("No se pudieron cargar estudiantes. Verifique el archivo.")

        elif opcion == "2":
            # === OPCIÓN 2: Filtrar ===
            # Verificar que haya datos cargados antes de filtrar
            if not estudiantes:
                print("Error: primero debe cargar los datos (opción 1).")
                continue

            # Guardar el resultado del filtro para poder exportarlo después
            ultimo_filtro = menu_filtrar(estudiantes)

        elif opcion == "3":
            # === OPCIÓN 3: Ordenar ===
            if not estudiantes:
                print("Error: primero debe cargar los datos (opción 1).")
                continue

            estudiantes = menu_ordenar(estudiantes)

        elif opcion == "4":
            # === OPCIÓN 4: Mostrar estadísticas ===
            if not estudiantes:
                print("Error: primero debe cargar los datos (opción 1).")
                continue

            stats = generar_estadisticas(estudiantes)

            print("\n--- Estadísticas Generales ---")
            print(f"Total de estudiantes: {stats['total_estudiantes']}")
            print(f"Promedio general: {stats['promedio_general']}")
            print(f"Edad máxima: {stats['edad_maxima']}")
            print(f"Edad mínima: {stats['edad_minima']}")
            print("Conteo por carrera:")
            # Recorrer el diccionario de conteo e imprimir cada carrera
            for carrera, cantidad in stats["conteo_por_carrera"].items():
                print(f"  {carrera}: {cantidad}")

        elif opcion == "5":
            # === OPCIÓN 5: Exportar resultados ===
            if not estudiantes:
                print("Error: primero debe cargar los datos (opción 1).")
                continue

            menu_exportar(estudiantes, ultimo_filtro)

        elif opcion == "6":
            # === OPCIÓN 6: Salir ===
            print("¡Hasta luego!")
            sys.exit(0)  # sys.exit(0) termina el programa sin errores (módulo 4)

        else:
            # Si el usuario ingresó algo que no es 1-6
            print("Opción no válida. Por favor ingrese un número del 1 al 6.")


# Esta línea hace que main() se ejecute solo cuando corremos este archivo directamente
# y NO cuando otro archivo lo importa (módulo 4: lo vieron con saludos.py)
if __name__ == "__main__":
    main()