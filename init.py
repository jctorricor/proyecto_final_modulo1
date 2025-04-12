from data_load.read_images import File
from crud.agregar import ProcessImage

file = File()
file._data_load('covid/images')
#file.show_data()
    
while True:
    print("-" * 54)
    print("\nGestionar imagenes de COVID-19 Radiography Database:\n")
    print("       1: Agregar nueva imagen")
    print("       2: Modificar imagen")
    print("       3: Eliminar imagen")
    print("       0: Salir\n")
    print("-" * 54)

    try:
        opcion = int(input("Opcion: "))

        if opcion == 1:
            print("Selecionaste Opcion 1")
        
            import os
            import shutil
            
            while True:
                print("Presione 0 para salir")
                origen = input("Ruta de la imagen:").strip()
                os.chdir("../nuevo")
                destino = os.getcwd()
                print(destino)
                
                try:
                    shutil.copy(origen, destino)
                    print(f"Archivo copiado de '{origen}' a '{destino}'")   
                    break                 
                except Exception as e:
                    print(f"Error al copiar: {e}")                    
                
                if origen == '0':
                    break                        
            
        elif opcion == 2:
            print("Selecionaste Opcion 2")
        elif opcion == 3:
            print("Selecionaste Opcion 3")
        elif opcion == 0:
            print("Selecionaste Opcion 0")
            break
        else:       
            print("Opcion no valida seleccione una opcion de la lista")
    except Exception as e:
        print("Opcion no valida seleccione una opcion de la lista")
        print("\nError: ", e, "\n")
