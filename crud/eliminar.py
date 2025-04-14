import os
from typing import Dict

class DeleteImage:
    """Clase para gestionar la eliminación de imágenes y sus metadatos."""
    
    def __init__(self, metadata: Dict[str, Dict]):
        """
        Inicializa el gestor de eliminación con los metadatos de las imágenes.

        Args:
            metadata (Dict[str, Dict]): Diccionario con metadatos de imágenes (nombre de archivo como clave).
        """
        self.metadata = metadata

    def list_images(self) -> None:
        """Muestra todas las imágenes disponibles."""
        if not self.metadata:
            print("No hay imágenes registradas.")
            return
        print("\nImágenes disponibles:")
        for i, (filename, info) in enumerate(self.metadata.items(), 1):
            print(f"{i}. Filename: {filename}, "
                  f"Path: {info.get('path', 'N/A')}, "
                  f"Size: {info.get('size', 'N/A')} bytes, "
                  f"Last Modified: {info.get('last_modified', 'N/A')}")

    def delete(self, filename: str) -> bool:
        """
        Elimina una imagen y sus metadatos según su nombre de archivo, incluyendo el archivo físico.

        Args:
            filename (str): Nombre del archivo de la imagen (e.g., 'covid-001.png').

        Returns:
            bool: True si la eliminación fue exitosa, False si hubo un error o se canceló.
        """
        try:
            if filename not in self.metadata:
                print(f"No se encontró la imagen con nombre {filename}.")
                return False

            image_info = self.metadata[filename]
            file_path = image_info.get("path", "")
            print(f"¿Está seguro de eliminar la imagen {filename}? (s/n)")
            confirmation = input().strip().lower()
            if confirmation != 's':
                print("Eliminación cancelada.")
                return False

            # Eliminar archivo físico
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Archivo {file_path} eliminado del disco.")
            else:
                print(f"Advertencia: El archivo {file_path} no se encontró en el disco.")

            # Eliminar del registro
            del self.metadata[filename]
            print(f"Imagen {filename} eliminada exitosamente del sistema.")
            return True

        except PermissionError:
            print(f"Error: No se tienen permisos para eliminar el archivo {file_path}.")
            return False
        except Exception as e:
            print(f"Error al eliminar la imagen: {str(e)}")
            return False