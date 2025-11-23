import os
import csv
import files

def restart():
    """
    Limpia la terminal según el sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():  # Diseño del menú principal
    print("""
 __________________________________________________
|                                                  |
|                  Menú principal                  |
|__________________________________________________|
|                                                  |
|   [1] Gestión de inventario                      |
|   [2] Estadisticas de inventario                 |
|   [3] Guardar CSV                                |
|   [4] Cargar CSV                                 |
|   [5] Salir                                      |
|__________________________________________________|
""")


def inventory_management():  # Diseño del menú de Gestión de inventario
    print("""
 ___________________________________________________
|                                                   |
|               Gestión de inventario               |
|___________________________________________________|
|                                                   |
|   [1] Mostrar Inventario                          |
|   [2] Agregar Producto                            |
|   [3] Buscar Producto                             |
|   [4] Actualizar Producto                         |
|   [5] Eliminar Producto                           |
|   [6] Volver al menú principal                    |
|___________________________________________________|
""")


def add_product_menu():  # Diseño dek menú de agregar productos
    print("""
 ____________________________________________________
|                                                    |
|                  Agregar producto                  |
|____________________________________________________|
|                                                    |
|  >> ID del producto                                |
|  >> Nombre del producto:                           |
|  >> Cantidad del producto:                         |
|  >> Precio del producto:                           |
|____________________________________________________|
""")


def show_inventory():
    """
    Muestra todo el inventario actual leyendo el archivo CSV.
    
    Si el archivo solo contiene encabezados o está vacío,
    muestra un mensaje indicando que no hay productos.
    """
    restart()

    # Construye la ruta completa del CSV actual para evitar errores.
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    # Lee todas las filas del archivo.
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        lines = list(reader)

    if len(lines) <= 1:  # Solo encabezado
        print("""
 ____________________________________________________
|                                                    |
|            ¡El inventario esta vacío!              |
|____________________________________________________|
""")
        input("\n/---Presione Enter para volver al menú de Gestión de inventario---/")
        return

    print("""
 _____________________________________________________
|                                                     |
|                 Inventario actual                   |
|_____________________________________________________|
""")

    # Imprime cada producto
    for row in lines[1:]:
        Id, Nombre, Cantidad, Precio = row
        print(f"ID:{Id} | Producto:{Nombre} | Cantidad:{Cantidad} | Precio:{Precio}")

    input("\n/---Presione Enter para volver al menú de gestión de inventario---/")


def add_product(Id, Nombre, Cantidad, Precio):
    """
    Agrega un nuevo producto al archivo CSV actual.
    
    - Verifica si el archivo existe.
    - Valida si el encabezado está correcto.
    - Agrega el producto como nueva fila.
    """
    # Construimos ruta del archivo
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    encabezado = "Id,Nombre,Cantidad,Precio"

    # Verifica si hay que crear el encabezado
    crear_encabezado = False

    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        crear_encabezado = True
    else:
        # Verifica si el encabezado es correcto
        with open(ruta, "r", encoding="utf-8") as archivo:
            if archivo.readline().strip() != encabezado:
                crear_encabezado = True

    # Si falta el encabezado, lo escribe
    if crear_encabezado:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(encabezado + "\n")

    # Agrega el producto al archivo
    with open(ruta, "a", encoding="utf-8", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([Id, Nombre, Cantidad, Precio])

    print(f"Producto {Nombre} agregado correctamente a {files.current_csv}")


def id_existe(Id):
    """
    Verifica si un ID ya existe en el archivo CSV.
    
    Returns:
        True si el ID ya está registrado.
        False si no existe o si el archivo está vacío.
    """
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    if not os.path.exists(ruta):
        return False

    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        rows = list(reader)

    # Recorre desde la segunda fila (productos)
    for row in rows[1:]:
        if row[0] == str(Id):
            return True

    return False


def pedir_entero(mensaje, minimo=0):
    """
    Solicita un número entero validado.
    
    - Solo permite enteros.
    - Valida valores mínimos.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"⚠ El número debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠ Debes ingresar un número entero válido.")


def pedir_float(mensaje, minimo=0):
    """
    Solicita un número flotante validado.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"⚠ El número debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠ Debes ingresar un número válido.")


def pedir_nombre(mensaje):
    """
    Solicita un nombre válido (solo letras y espacios).
    """
    while True:
        nombre = input(mensaje).strip()
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("⚠ El nombre solo puede tener letras.")


def search_product():
    """
    Busca un producto por ID y lo muestra.
    """
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        reader = csv.reader(archivo)
        lines = list(reader)

    if len(lines) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|            ¡El inventario esta vacío!              |
|____________________________________________________|
""")
        input("\n/---Presione Enter para volver al menú de gestión de inventario")
        return
    
    product_id = input("Ingrese el Id del producto a buscar: ")
    found = False

    for row in lines[1:]:
        Id, Nombre, Cantidad, Precio = row

        if Id == product_id:
            print("""
 _____________________________________________________
|                                                     |
|                ¡Producto encontrado!                |
|_____________________________________________________|
""")
            print(f"ID: {Id} | Producto: {Nombre} | Cantidad: {Cantidad} | Precio: {Precio}")
            found = True
            break

    if not found:
        print(f"No se encontró ningún producto con el Id {product_id}")
        
    input("\n/---Presione Enter para volver al menú de Gestión de inventario---/")


def update_product():
    """
    Actualiza los datos de un producto existente.
    
    Permite modificar nombre, cantidad o precio.
    Mantiene los valores actuales si el usuario presiona Enter.
    """
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        reader = csv.reader(archivo)
        rows = list(reader)

    if len(rows) <= 1:
        print("""
 ____________________________________________________
|                                                    |
|            ¡El inventario esta vacío!              |
|____________________________________________________|
""")
        input("\n/---Presione Enter para volver al menú de gestión de inventario")
        return
    
    product_id = input("Ingrese el Id del producto a actualizar: ")
    found = False
    
    for i, row in enumerate(rows[1:], start=1):
        Id, Nombre, Cantidad, Precio = row

        if Id == product_id:
            print("""
 _____________________________________________________
|                                                     |
|                ¡Producto encontrado!                |
|_____________________________________________________|
""")
            print(f"Nombre: {Nombre} | Cantidad: {Cantidad} | Precio: {Precio}")

            print("\nSi no quieres modificar algo, presiona Enter.")

            nuevo_nombre = input(f"Ingresa el nombre nuevo [{Nombre}]: ") or Nombre
            nueva_cantidad = input(f"Ingrese la nueva cantidad [{Cantidad}]: ") or Cantidad
            nuevo_precio = input(f"Ingrese el nuevo precio [{Precio}]: ") or Precio

            rows[i] = [Id, nuevo_nombre, nueva_cantidad, nuevo_precio]
            found = True
            break

    if not found:
        print(f"No se encontró ningún producto con ID {product_id}")
        input("\nPresiona Enter para volver al menú...")
        return

    # Sobrescribe archivo actualizado
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(rows)
    
    print("\n¡Producto actualizado correctamente!")
    input("\nPresiona Enter para volver al menú...")


def delete_product():
    """
    Elimina un producto del inventario por ID.
    Requiere confirmación antes de borrar.
    """
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)
    
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        reader = csv.reader(archivo)
        rows = list(reader)
    
    if len(rows) <= 1:
        print("""
 _____________________________________________________
|                                                     |
|                  ¡Inventario vacio!                 |
|_____________________________________________________|
""")
        input("\nPresiona Enter para volver al menú...")
        return

    product_id = input("Ingrese el Id del producto a eliminar: ")
    found = False

    for i, row in enumerate(rows[1:], start=1):
        Id, Nombre, Cantidad, Precio = row

        if Id == product_id:
            print(f"Producto encontrado: ID:{Id} | Nombre:{Nombre} | Cantidad:{Cantidad} | Precio:{Precio}")

            confirm = input("¿Seguro que quieres eliminar este producto? (Si/No): ").lower()
            if confirm == "si":
                rows.pop(i)
                found = True
                break

    if not found:
        print(f"No se encontró ningún producto con ID {product_id}")
        input("\nPresiona Enter para volver al menú...")
        return

    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(rows)
    
    print("Producto eliminado correctamente.")
    input("\nPresiona Enter para volver al menú...")


def stats_inventory():
    """
    Calcula estadísticas del inventario:
    - Unidades totales
    - Valor total
    - Producto más caro
    - Producto con mayor stock
    """
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    # Carga los productos
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        reader = csv.DictReader(archivo)
        productos = list(reader)

    if not productos:
        print("""
 _____________________________________________________
|                                                     |
|                  ¡Inventario vacio!                 |
|_____________________________________________________|
""")
        input("Presiona Enter para volver al menú...")
        return

    # Convierte valores para operar
    for p in productos:
        p["Cantidad"] = int(p["Cantidad"])
        p["Precio"] = float(p["Precio"])

    subtotal = lambda p: p["Precio"] * p["Cantidad"]

    unidades_totales = sum(p["Cantidad"] for p in productos)
    valor_total = sum(subtotal(p) for p in productos)
    producto_mas_caro = max(productos, key=lambda p: p["Precio"])
    producto_mayor_stock = max(productos, key=lambda p: p["Cantidad"])

    print("""
 ____________________________________________________
|                                                    |
|              Estadísticas del inventario           |
|____________________________________________________|
""")
    print(f"Unidades totales en inventario: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Producto más caro: {producto_mas_caro['Nombre']} - ${producto_mas_caro['Precio']:.2f}")
    print(f"Producto con mayor stock: {producto_mayor_stock['Nombre']} - {producto_mayor_stock['Cantidad']} unidades")
    
    input("\nPresiona Enter para volver al menú...")
