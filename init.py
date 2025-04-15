from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.modificar import renombrar_archivo
from crud.eliminar import DeleteImage
import os 

file = File()

if not hasattr(file, 'metadata'):
    file.metadata = {}

def recargar_metadatos(file_instance):
    file_instance.metadata = {}  # Limpiar metadatos existentes
    cargar_archivos()

def cargar_archivos():
    base_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "covid"))
    for folder in ["images", "nuevo"]:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            for f in os.listdir(folder_path):
                file_path = os.path.join(folder_path, f)
                if os.path.isfile(file_path):
                    file.metadata[f] = {
                        'filename': f,
                        'path': file_path,
                        'size': os.path.getsize(file_path),
                        'last_modified': os.path.getmtime(file_path)
                    }

cargar_archivos()       
    
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
            p = ProcessImage()
            pathfile = p.copiar()
            print(pathfile)
            procesado = file._data_process(pathfile)
            if procesado:      
                file._del_file_procesado(pathfile)
                recargar_metadatos(file)  # Actualizar metadatos después de agregar
            
        elif opcion == 2:
            print("Seleccionaste Opcion 2")
            renombrar_archivo()
            recargar_metadatos(file)
            
        elif opcion == 3:
            print("Seleccionaste Opción 3")
            d = DeleteImage(file.metadata)  # Usar file.metadata
            d.list_images()
            filename = input("Ingrese el nombre del archivo a eliminar (e.g., covid-001.png): ")
            d.delete(filename)
            recargar_metadatos(file)  # Actualizar metadatos después de eliminar
            
        elif opcion == 4:
            print("\n" + "📄 LISTA SIMPLE DE ARCHIVOS ".center(50, '='))
            if file.metadata:
                for i, (filename, data) in enumerate(file.metadata.items(), 1):
                    print(f"{i}. {filename} - {data.get('size', '?')} bytes")
            else:
                print("No hay archivos cargados")
            
            
        elif opcion == 0:
            print("Seleccionaste Opción 0")
            break
            
        else:
            print("Opción no válida, seleccione una opción de la lista")
            
    except ValueError:
        print("Opción no válida, ingrese un número.")
    except Exception as e:
        print("ERROR: ", e)