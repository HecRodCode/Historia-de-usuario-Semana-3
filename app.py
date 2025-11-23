import os 
import csv
import services
import files


# BUCLE PRINCIPAL DEL PROGRAMA
while True:
    services.restart()        # Limpia pantalla (si lo tienes así en services)
    services.main_menu()      # Muestra menú principal

    # Validación de opción del menú principal
    try: 
        option = int(input("Ingresa una opción:"))
    except ValueError:
        print("¡Ingresa una opción valida!")
        continue

    # MANEJO DEL MENÚ PRINCIPAL
    match option:

        # GESTIÓN DE INVENTARIO
        case 1:
            while True:
                services.restart()
                services.inventory_management()  # Muestra submenú de inventario

                # Validación de opción del submenú
                try:
                    option1 = int(input("Ingresa una opción:"))
                except ValueError:
                    print("¡Ingresa una opción valida!")
                    continue

                
                # MANEJO DEL SUBMENÚ DE INVENTARIO
                match option1:

                    # Mostrar inventario
                    case 1:
                        services.show_inventory()

                    # Agregar producto
                    case 2:
                        while True:
                            services.restart()
                            services.add_product_menu()

                            # Pedir ID validando que no exista
                            while True:
                                Id = services.pedir_entero("Ingrese el ID del producto:", minimo=1)

                                if services.id_existe(Id):
                                    print("⚠ Ese ID ya existe. Ingresa otro.")
                                    continue
                                break

                            # Pedir y validar los demás datos
                            Nombre = services.pedir_nombre("Ingrese el Nombre del producto:")
                            Cantidad = services.pedir_entero("Ingrese la cantidad del producto:", minimo=0)
                            Precio = services.pedir_float("Ingrese el precio del producto:", minimo=1)
                            
                            # Agregar producto al inventario
                            services.add_product(Id, Nombre, Cantidad, Precio)

                            input("\n Producto agregado correctamente - Presiona Enter para continuar")
                            break

                    # Buscar producto
                    case 3:
                        services.restart()
                        services.search_product()

                    # Actualizar producto
                    case 4:
                        services.restart()
                        services.update_product()

                    # Eliminar producto
                    case 5:
                        services.restart()
                        services.delete_product()

                    # Volver al menú principal
                    case 6:
                        break

        # Mostrar estadísticas
        case 2:
            services.restart()
            services.stats_inventory()

        # Guardar inventario en CSV
        case 3:
            files.save_inventory_csv()

        # Cargar inventario desde CSV
        case 4:
            files.load_inventory_csv()

        # Salir del programa
        case 5:
            print("Saliendo del programa...")
            break