import os
import shutil

def copiar_archivo(origen, destino):
    # Verificar si el archivo origen existe
    if not os.path.exists(origen):
        print(f"Error: El archivo origen '{origen}' no existe")
        return False
    
    # Verificar si es un archivo (no directorio)
    if not os.path.isfile(origen):
        print(f"Error: '{origen}' no es un archivo")
        return False
    
    # Verificar si el directorio destino existe
    directorio_destino = os.path.dirname(destino)
    if directorio_destino and not os.path.exists(directorio_destino):
        print(f"Error: El directorio destino '{directorio_destino}' no existe")
        return False
    
    # Copiar el archivo
    try:
        shutil.copyfile(origen, destino)
        print(f"Archivo copiado de '{origen}' a '{destino}'")
        return True
    except Exception as e:
        print(f"Error al copiar: {e}")
        return False

# Ejemplo de uso
origen = r'c:\Users\jctorrico\proyecto_final_modulo1\covid\images\COVID-94.png'
destino = r'c:\Users\jctorrico\proyecto_final_modulo1\covid\nuevo\COVID-94.png'

copiar_archivo(origen, destino)