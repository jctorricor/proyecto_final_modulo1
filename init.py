from data_load.read_images import File

file = File()
file._data_load('covid/images')
#file.show_data()
    
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
        print("Selecionaste Opcion 1")
    elif opcion == 2:
        print("Selecionaste Opcion 2")
    elif opcion == 3:
        print("Selecionaste Opcion 3")
    elif opcion == 0:
        print("Selecionaste Opcion 0")
        break
    else:       
        print("Opcion no valida seleccione una opcion de la lista")
                
