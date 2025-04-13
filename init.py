while True:
    print("-" * 54)
    print("\nGestionar imagenes de COVID-19 Radiography Database:\n")
    print("       1: Agregar nueva imagen")
    print("       2: Modificar imagen")
    print("       3: Eliminar imagen")
    print("       4: Mostrar imagenes cargadas")
    print("       0: Salir\n")
    print("-" * 54)

    try:
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
        print("\nError: ", e, "\n")
