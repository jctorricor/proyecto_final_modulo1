import os

def mostrar_menu_carpetas():
    print("SELECCIONA CARPETA".center(50, '='))
    print("1. images")
    print("2. nuevo")
    print("0. Salir")

#esta funcion evita que el formato se pierda al renombrar el archivo
def extension(nombre_archivo):
    """Extrae la extensión del archivo (incluyendo el punto)"""
    return os.path.splitext(nombre_archivo)[1]

def lista_archivos(ruta):
    try:
        archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]
        if not archivos:
            print("\n No se encontraron archivos en esta carpeta")
            return None
        
        print("\n ARCHIVOS DISPONIBLES:")
        for i, archivo in enumerate(archivos, 1):
            print(f"{i:>2}. {archivo}")
        return archivos
    except FileNotFoundError:
        print(f"\n ERROR: La carpeta no existe: {ruta}")
        return None

def renombrar_archivo():
    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    while True:
        mostrar_menu_carpetas()
        opcion = input("\n  Seleccione carpeta (0-2): ").strip()
        
        if opcion == "0":
            print("\n Programa terminado")
            break
            
        if opcion not in ["1", "2"]:
            print("\n ERROR: Opción no válida")
            continue
            
        subcarpeta = "images" if opcion == "1" else "nuevo"
        ruta_completa = os.path.join(ruta_base, "covid", subcarpeta)
        
        archivos = lista_archivos(ruta_completa)
        if not archivos:
            continue
            
        try:
            seleccion = int(input("\n🔢 Ingrese número de archivo (0 para cancelar): "))
            if seleccion == 0:
                continue
            if seleccion < 1 or seleccion > len(archivos):
                print("\n ERROR: Número fuera de rango")
                continue
        except ValueError:
            print("\n ERROR: Debe ingresar un número válido")
            continue
            
        archivo_original = archivos[seleccion-1]
        extension_actual = extension(archivo_original)
        
        print(f"\n  Archivo seleccionado: {archivo_original}")
        print(f" Extensión detectada: {extension_actual}")
        
        nuevo_nombre_base = input("\n Ingrese NUEVO NOMBRE (sin extensión): ").strip()
        
        if not nuevo_nombre_base:
            print("\n ERROR: El nombre no puede estar vacío")
            continue
            
        nuevo_nombre_completo = f"{nuevo_nombre_base}{extension_actual}"
        
        confirmacion = input(f"\n¿Confirmar cambio de '{archivo_original}' a '{nuevo_nombre_completo}'? (s/n): ").lower()
        if confirmacion != 's':
            print("\n Operación cancelada")
            continue
            
        try:
            os.rename(
                os.path.join(ruta_completa, archivo_original),
                os.path.join(ruta_completa, nuevo_nombre_completo)
            )
            print(f"\n ÉXITO: Archivo renombrado correctamente")
            print(f"   Anterior: {archivo_original}")
            print(f"   Nuevo: {nuevo_nombre_completo}")
        except Exception as e:
            print(f"\n ERROR: No se pudo renombrar - {str(e)}")

if __name__ == "__main__":
    renombrar_archivo()