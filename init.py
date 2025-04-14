from data_load.read_images import File
from crud.agregar import ProcessImage
from crud.modificar import renombrar_archivo

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
            recargar_metadatos(file)
                             
    elif opcion == 3:
        print("Selecionaste Opcion 3")
    elif opcion == 4:
            #file.show_data()
        print("\n" + "📄 LISTA SIMPLE DE ARCHIVOS ".center(50, '='))
        if file.metadata:
            for i, (filename, data) in enumerate(file.metadata.items(), 1):
                print(f"{i}. {filename} - {data.get('size', '?')} bytes")
        else:
             print("No hay archivos cargados")
            
        input("\nPresione Enter para ver el formato show_data()...")
            
        # Segunda visualización (método show_data)
        print("\n" + "📊 VISUALIZACIÓN CON SHOW_DATA() ".center(50, '='))
        file.show_data()
    elif opcion == 0:
        print("Selecionaste Opcion 0")
        break
            