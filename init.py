while True:
    print("-" * 50)
    print("Gestionar imagenes de COVID-19 Radiography Database:")
    print("       1: Agregar nueva imagen")
    print("       2: Modificar imagen")
    print("       3: Eliminar imagen")
    print("       0: Salir")
    print("-" * 50)

    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("Seleecionaste Opcion 1")
    elif opcion == 2:
        print("Seleecionaste Opcion 2")
    elif opcion == 3:
        print("Seleecionaste Opcion 3")
    elif opcion == 0:
        print("Seleecionaste Opcion 0")
        break
    else:       
        print("Opcion no valida seleccione una opcion de la lista")
                
