from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.modificar import renombrar_archivo
from crud.eliminar import DeleteImage
import os 

file = File()

if not hasattr(file, 'metadata'):
    file.metadata = {}

def recargar_metadatos(file_instance):
    """
    Reinicia y vuelve a cargar los metadatos para una instancia dada.

    Primero, vacía el diccionario `metadata` de la `file_instance` proporcionada.
    Luego, llama a la función `cargar_archivos()` para escanear los
    directorios predefinidos ('covid/images', 'covid/nuevo') y poblar
    nuevamente los metadatos.

    Advertencia:
        Esta función asume que `cargar_archivos()` modificará los metadatos
        de una instancia específica (posiblemente una instancia global `file`
        a la que `cargar_archivos` tiene acceso), que puede o no ser la
        misma `file_instance` pasada como argumento, dependiendo de cómo
        esté definida `cargar_archivos` y la variable `file` que usa.
        Actualmente, `cargar_archivos` parece modificar una variable `file`
        accesible globalmente.

    Parameters
    ----------
    file_instance : object
        Una instancia de una clase (presumiblemente la clase `File` o similar)
        que tiene un atributo `metadata` (un diccionario) que será limpiado.
    """
    file_instance.metadata = {}  # Limpiar metadatos existentes
    cargar_archivos()

def cargar_archivos():
    """
    Escanea directorios específicos y carga metadatos de archivos en una instancia `file`.

    Busca los subdirectorios 'images' y 'nuevo' dentro de un directorio 'covid'
    ubicado junto al script actual (`__file__`). Para cada archivo encontrado
    dentro de estos subdirectorios, extrae sus metadatos (nombre, ruta completa,
    tamaño y fecha de última modificación) y los almacena en el diccionario
    `metadata` de una variable predefinida llamada `file`.

    Notas:
        - Esta función depende de la existencia de una variable llamada `file`
          en el ámbito donde se llama, y que esta variable tenga un atributo
          `metadata` (un diccionario). Modifica directamente `file.metadata`.
        - La ruta base se calcula relativa a la ubicación del archivo de script
          que contiene esta función.
        - Los directorios buscados son estrictamente `covid/images` y `covid/nuevo`.
        - No devuelve ningún valor (`None`).

    Side Effects:
        - Modifica el contenido del atributo `file.metadata`.

    Raises:
        - Potencialmente `FileNotFoundError` si `__file__` no está definido
          correctamente (poco común en scripts normales).
        - Potencialmente `OSError` si hay problemas de permisos al listar
          directorios o acceder a archivos.
    """
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
            recargar_metadatos(file)
            
        elif opcion == 4:
            print("Seleccionaste Opcion 4")
            print("\nLISTA SIMPLE DE ARCHIVOS ".center(50, '='))
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