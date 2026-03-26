""" 
Módulo de inventario.

Permite agregar productos al inventario y mostrarlos en pantalla.
Cada producto contiene nombre, precio y cantidad.
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente")

def mostrar_inventario (inventario):
    """Muestra todos los productos almacenados en el inventario"""

    if not inventario:
        print("No hay nada en el inventario")
    else:
        print("\n--- INVENTARIO ---\n")
        for producto_registrado in inventario:
            print("Producto:", producto_registrado["nombre"],
            "|Precio:", producto_registrado["precio"], 
            "|Cantidad:", producto_registrado["cantidad"],"\n")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
        else:
            return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto no encontrado")
        return
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    print("Producto actualizado")

def eliminar_producto(inventario, nombre):
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            inventario.pop(i)
            print("Producto eliminado")
            return
        else:
            print("Producto no encontrado")

def calcular_estadisticas(inventario):
    """
    Calcula y muestra estadísticas del inventario.

    Parámetros:
        inventario (list[dict]): lista de productos.
            Cada producto debe tener las claves:
            - "nombre" (str)
            - "precio" (float)
            - "cantidad" (int)

    Retorno:
        dict | None: diccionario con las métricas calculadas si hay productos;
        en caso contrario, retorna None.
    """

    if not inventario:
        print("No hay productos para calcular estadísticas.\n")
        return None

    # Lambda para calcular el subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(producto["cantidad"] for producto in inventario)
    valor_total = sum(subtotal(producto) for producto in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    estadisticas = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"],
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"],
        },
    }

    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Productos registrados: {len(inventario)}")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(
        f"Producto más caro: {producto_mas_caro['nombre']} "
        f"(${producto_mas_caro['precio']:,.2f})"
    )
    print(
        f"Producto con mayor stock: {producto_mayor_stock['nombre']} "
        f"({producto_mayor_stock['cantidad']} unidades)\n"
    )

    return estadisticas
