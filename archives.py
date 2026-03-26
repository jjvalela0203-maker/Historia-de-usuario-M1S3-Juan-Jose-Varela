"""
Módulo de persistencia en archivos CSV.

Permite guardar y cargar el inventario en un archivo CSV.
"""
from services import clear_screen

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list[dict]): lista de productos con estructura:
        {"nombre": str, "precio": float, "cantidad": int}
        ruta (str): ruta donde se guardará el archivo
        incluir_header (bool): indica si se escribe el encabezado

    Retorno:
        None
    """
    if not inventario:
        print("No hay productos en el inventario para guardar.\n")
        input("Presione enter para volver al menu")
        clear_screen()
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            if incluir_header:
                archivo.write("nombre,precio,cantidad\n")
            for producto in inventario:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print(f"Inventario guardado en: {ruta}\n")
        input("Presione enter para volver al menu")
        clear_screen()

    except PermissionError:
        print("Error: No tienes permisos para escribir en esa ubicación.\n")
    except FileNotFoundError:
        print("Error: La ruta especificada no existe.\n")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")

def cargar_csv(ruta):
    """
    Carga un archivo CSV y retorna una lista de productos válidos.

    Parámetros:
        ruta (str): ruta del archivo CSV

    Retorno:
        tuple: (lista_productos, filas_invalidas)
    """

    inventario_cargado = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:

            # Leer todas las líneas
            lineas = archivo.readlines()

            # Validar archivo vacío
            if not lineas:
                print("El archivo está vacío")
                input("\nPresione enter para volver al menu")
                clear_screen()
                return [], 0

            # Validar encabezado
            encabezado = lineas[0].strip()
            if encabezado != "nombre,precio,cantidad":
                print("Encabezado inválido")
                input("\nPresione enter para volver al menu")
                clear_screen()
                return [], 0

            # Procesar filas
            for linea in lineas[1:]:
                partes = linea.strip().split(",")

                # Validar columnas
                if len(partes) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = partes

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    # Validar negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    inventario_cargado.append(producto)

                except ValueError:
                    filas_invalidas += 1
                    continue

        return inventario_cargado, filas_invalidas

    except FileNotFoundError:
        print("Error: El archivo no existe")
        input("\nPresione enter para volver al menu")
        clear_screen()
        return [], 0

    except UnicodeDecodeError:
        print("Error: Problema de codificación del archivo")
        input("\nPresione enter para volver al menu")
        clear_screen()
        return [], 0

    except Exception as e:
        print(f"Error inesperado: {e}")
        input("\nPresione enter para volver al menu")
        clear_screen()
        return [], 0
