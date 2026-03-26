"""
Módulo principal del sistema de gestión de inventario.

Este módulo controla el flujo de ejecución del programa mediante
un menú interactivo. Permite al usuario agregar productos, mostrar
el inventario y calcular estadísticas, utilizando funciones de
otros módulos.

El programa se ejecuta de forma continua hasta que el usuario
selecciona la opción de salida.
"""
from services import (agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas)
from archives import (guardar_csv, cargar_csv)
import os

inventario =[]

def mostrar_menu():
    logo= r"""
    ██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    ██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝     ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║       ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
                                                                                                                                    """
    
    
    print(logo)
    print("\n", "=" *30, "MENU", "=" *30, "\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

active=True
while active:
    mostrar_menu()

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número válido")
        continue

    if opcion == 1:
        os.system('clear')
        print("\n","="*30,"Agregar un producto","="*30,"\n")
        
        nombre = input("Nombre: ")

        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("\nPrecio o cantidad inválidos")
            input("\nPresione enter para volver al menu")
            os.system('clear')
            continue

        if precio < 0 or cantidad < 0:
            print("\nNo se permiten valores negativos")
            continue

        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == 2:
        os.system('clear')

        print("\n","="*30,"INVENTARIO","="*30,"\n")
        mostrar_inventario(inventario)

    elif opcion == 3:
        os.system('clear')
        print("\n","="*30,"Buscar un producto","="*30,"\n")
        nombre = input("Ingrese el nombre del producto: ")
        producto = buscar_producto(inventario, nombre)

        if not producto:
            print("\n","="*30,"Buscar un producto","="*30,"\n")
            print("Producto no encontrado")
            input("Presione enter para volver al menu")
            os.system('clear')


    elif opcion == 4:
        os.system('clear')
        print("\n","="*30,"Actualizar un producto","="*30,"\n")
        nombre = input("Nombre del producto a actualizar: ")

        try:
            precio = input("Nuevo precio (Enter para omitir): ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")

            nuevo_precio = float(precio) if precio else None
            nueva_cantidad = int(cantidad) if cantidad else None
        except ValueError:
            print("\nDatos inválidos")
            input("\nPresione enter para volver al menu")
            os.system('clear')
            continue

        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == 5:
        os.system('clear')
        print("\n","="*30,"Eliminar un producto","="*30,"\n")
        nombre = input("Nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 7:
        ruta = input("Ingrese el nombre del archivo (ej: inventario.csv): ")
        guardar_csv(inventario, ruta)

    elif opcion == 8:
        ruta = input("Ingrese la ruta del archivo CSV: ")

        nuevos_productos, errores = cargar_csv(ruta)

        if not nuevos_productos:
            print("No se cargaron productos")
            continue

        decision = input("¿Sobrescribir inventario actual? (S/N): ").lower()

        if decision == "s":
            inventario.clear()
            inventario.extend(nuevos_productos)
            print("Inventario reemplazado")

        else:  # Fusión
            for nuevo in nuevos_productos:
                existente = buscar_producto(inventario, nuevo["nombre"])

                if existente:
                    existente["cantidad"] += nuevo["cantidad"]
                    existente["precio"] = nuevo["precio"]
                else:
                    inventario.append(nuevo)

            print("Inventario fusionado")

        print(f"Productos cargados: {len(nuevos_productos)}")
        print(f"Filas inválidas: {errores}")

    elif opcion == 9:
        print("Saliendo del programa...")
        active=False
