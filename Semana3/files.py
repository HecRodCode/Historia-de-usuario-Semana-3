import os
import csv
import files   # <- Si esto está dentro de files.py quítalo. Solo úsalo si estás en otra carpeta.

# Archivo CSV por defecto
current_csv = "inventory.csv"


def set_current_csv(nombre):
    """
    Cambia el archivo CSV actual donde se guarda el inventario.
    Si el nombre no termina en .csv, se agrega automáticamente.
    """
    global current_csv

    if not nombre.endswith(".csv"):
        nombre += ".csv"
    
    current_csv = nombre


def save_inventory_csv():
    """
    Guarda (reescribe) el inventario actual en el archivo CSV.
    Verifica que el archivo exista y tenga datos antes de guardar.
    """
    # Construye la ruta completa del archivo CSV
    ruta = os.path.join(os.path.dirname(__file__), current_csv)

    try:
        # Leemos el archivo actual para verificar contenido
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            reader = csv.reader(archivo)
            rows = list(reader)

        if len(rows) <= 1:  # Si no hay productos
            print("""
 ____________________________________________________
|                                                    |
|              ¡El inventario está vacío!            |
|____________________________________________________|
""")
            input("Presiona Enter para continuar...")
            return

    except FileNotFoundError:
        print("El archivo actual no existe, no se puede guardar.")
        input("Presiona Enter...")
        return

    # Reescribir archivo correctamente
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            writer = csv.writer(archivo)

            # Encabezado obligatorio
            writer.writerow(["Id", "Nombre", "Cantidad", "Precio"])

            for i, row in enumerate(rows):
                # Si el archivo ya tenía encabezado lo saltamos
                if i == 0 and (row[0].lower() == "id"):
                    continue
                writer.writerow(row)

        print(f"Inventario guardado correctamente en: {ruta}")

    except PermissionError:
        print("No se pudo guardar. Permisos denegados.")

    except:
        print("Ocurrió un error inesperado al guardar.")

    input("\nPresiona Enter para continuar...")


def load_inventory_csv():
    """
    Carga un archivo CSV de inventario.
    Si no existe, lo crea con el encabezado correcto.
    También verifica si el encabezado es válido y lo corrige si es necesario.
    """
    nuevo_archivo = input("Ingresa el nombre del archivo CSV a cargar: ")

    files.set_current_csv(nuevo_archivo)
    ruta = os.path.join(os.path.dirname(__file__), files.current_csv)

    # Si no existe → crearlo nuevo
    if not os.path.exists(ruta):
        print(f"""
 ____________________________________________________
|                                                    |
|  ¡El archivo {files.current_csv} NO existe!        |
|  Se creará uno nuevo con encabezado.               |
|____________________________________________________|
""")
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("Id,Nombre,Cantidad,Precio\n")

        input("Presiona Enter para continuar...")
        return

    # Validamos el encabezado
    with open(ruta, "r", encoding="utf-8") as archivo:
        primera_linea = archivo.readline().strip()

    encabezado_correcto = "Id,Nombre,Cantidad,Precio"

    # Corrigir encabezado en caso de que esté mal
    if primera_linea != encabezado_correcto:
        print("""
 ____________________________________________________
|                                                    |
|  ⚠ El archivo NO tenía encabezado correcto         |
|  → Se le añadió automáticamente.                   |
|____________________________________________________|
""")
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(encabezado_correcto + "\n" + contenido)

    print(f"Archivo cargado correctamente: {files.current_csv}")
    input("Presiona Enter para continuar...")
