import os
import time

def mostrar_menu_carpetas():
    """
    Muestra un menú de selección de carpetas al usuario.
    """
    print("SELECCIONA CARPETA".center(50, '='))
    print("1. images")
    print("2. nuevo")
    print("0. Salir")

#esta funcion evita que el formato se pierda al renombrar el archivo
def extension(nombre_archivo):
    """
    Extrae la extensión del archivo (incluyendo el punto) de un nombre de archivo.

    Args:
        nombre_archivo (str): El nombre del archivo.

    Returns:
        str: La extensión del archivo, incluyendo el punto (ej: ".txt", ".jpg").  Retorna una cadena vacía si no tiene extensión.
    """
    return os.path.splitext(nombre_archivo)[1]

def lista_archivos(ruta):
    """
    Lista los archivos en una ruta dada.

    Args:
        ruta (str): La ruta del directorio a listar.

    Returns:
        list: Una lista de nombres de archivos en la ruta, o None si la ruta no existe o está vacía.
    """
    try:
        archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]
        if not archivos:
            print("\n No hay archivos en esta carpeta")
            return None
        
        print("\n ARCHIVOS DISPONIBLES:")
        for i, archivo in enumerate(archivos, 1):
            print(f"{i:>2}. {archivo}")
        return archivos
    except FileNotFoundError:
        print(f"\n Error: La carpeta no existe: {ruta}")
        return None

def renombrar_archivo(file_instance=None):
    """
    Permite al usuario seleccionar un archivo de una carpeta específica y renombrarlo.

    Args:
        file_instance (object, optional): Una instancia de un objeto que contiene metadatos de archivos. Defaults to None.
                                          Si se proporciona, los metadatos se actualizan después de renombrar el archivo.

    Returns:
        bool: True si el proceso de renombrado fue exitoso, False si hubo un error o el usuario canceló.
    """
    # Ruta absoluta garantizada para Windows
    proyecto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    covid_dir = os.path.normpath(os.path.join(proyecto_dir, "covid"))
    
    print(f"\nDEBUG: Ruta covid confirmada: {covid_dir}")
    print(f"DEBUG: Contenido real: {os.listdir(covid_dir)}")

    while True:
        print("\n" + "="*50)
        print("MODIFICAR ARCHIVO".center(50))
        print("1. images\n2. nuevo\n0. Volver")
        
        opcion = input("\nSeleccione carpeta (0-2): ").strip()
        
        if opcion == "0":
            return True
            
        if opcion not in ["1", "2"]:
            print("\n Opción no válida")
            continue
            
        subcarpeta = "images" if opcion == "1" else "nuevo"
        target_dir = os.path.normpath(os.path.join(covid_dir, subcarpeta))
        
        # Verificación EXTREMA
        if not os.path.exists(target_dir):
            print(f"\n ERROR: No existe la carpeta: {target_dir}")
            continue
            
        # Listado SEGURO de archivos
        archivos = []
        for f in os.listdir(target_dir):
            full_path = os.path.join(target_dir, f)
            if os.path.isfile(full_path):
                archivos.append(f)
        
        if not archivos:
            print(f"\n No hay archivos en {subcarpeta}/")
            continue
            
        print("\n Archivos disponibles:")
        for i, archivo in enumerate(archivos, 1):
            print(f"{i}. {archivo}")
            
        # Validación ROBUSTA
        try:
            seleccion = int(input("\nNúmero de archivo (0 para cancelar): "))
            if seleccion == 0:
                continue
            archivo_original = archivos[seleccion-1]
        except (ValueError, IndexError):
            print("\n Selección inválida")
            continue
            
        # Proceso de renombrado
        nombre_base, ext = os.path.splitext(archivo_original)
        nuevo_nombre = input("Nuevo nombre (sin extensión): ").strip()
        
        if not nuevo_nombre:
            print("\n El nombre no puede estar vacío")
            continue
            
        nuevo_nombre_completo = f"{nuevo_nombre}{ext}"
        vieja_ruta = os.path.join(target_dir, archivo_original)
        nueva_ruta = os.path.join(target_dir, nuevo_nombre_completo)
        
        try:
            # 1. Renombrar físicamente
            os.rename(vieja_ruta, nueva_ruta)
            print(f"\n Archivo renombrado: {archivo_original} → {nuevo_nombre_completo}")
            
            # 2. Actualización OBLIGATORIA de metadata
            if file_instance:
                if hasattr(file_instance, 'metadata') and archivo_original in file_instance.metadata:
                    file_instance.metadata[nuevo_nombre_completo] = file_instance.metadata.pop(archivo_original)
                    file_instance.metadata[nuevo_nombre_completo]['filename'] = nuevo_nombre_completo
                    file_instance.metadata[nuevo_nombre_completo]['path'] = nueva_ruta
                    file_instance.metadata[nuevo_nombre_completo]['size'] = os.path.getsize(nueva_ruta)
                    file_instance.metadata[nuevo_nombre_completo]['last_modified'] = os.path.getmtime(nueva_ruta)
                
                # Eliminar entrada vieja SI existe
                if archivo_original in file_instance.metadata:
                    del file_instance.metadata[archivo_original]
                
                # Crear NUEVA entrada con datos actualizados
                file_instance.metadata[nuevo_nombre_completo] = {
                    'filename': nuevo_nombre_completo,
                    'path': nueva_ruta,
                    'size': os.path.getsize(nueva_ruta),
                    'last_modified': os.path.getmtime(nueva_ruta)
                }
                print(" Metadata actualizada CORRECTAMENTE")
            
            # 3. Verificación INMEDIATA
            print("\n🔥 VERIFICACIÓN:")
            print(f"Archivo físico: {'EXISTE' if os.path.exists(nueva_ruta) else 'NO EXISTE'}")
            if file_instance and hasattr(file_instance, 'metadata'):
                print(f"En metadata: {'SÍ' if nuevo_nombre_completo in file_instance.metadata else 'NO'}")
            
            return True
            
        except Exception as e:
            print(f"\n Error al renombrar: {str(e)}")
            return False

if __name__ == "__main__":
    renombrar_archivo()