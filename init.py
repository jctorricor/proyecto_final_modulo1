from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.modificar import renombrar_archivo

file = File()
file._data_load()
#file.show_data()
    
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
    except Exception as e:
        print("ERROR: ", e)
        
        if opcion == 1:
            p = ProcessImage()
            pathfile = p.copiar() 
            print(pathfile)
            procesado = file._data_process(pathfile)
            
            if procesado:      
                file._del_file_procesado(pathfile)            
        
        elif opcion == 2:
            print("Selecionaste Opcion 2")
            renombrar_archivo()
             
        elif opcion == 3:
            print("Selecionaste Opcion 3")
        elif opcion == 4:
            file.show_data()
        elif opcion == 0:
            print("Selecionaste Opcion 0")
            break
            