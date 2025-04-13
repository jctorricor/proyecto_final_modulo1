import os
from typing import Dict, Optional

class DeleteImage:
    """Clase para gestionar la eliminación de imágenes y sus metadatos."""
    
    def __init__(self, data: Dict[str, Dict]):
        """
        Inicializa el gestor de eliminación con los datos cargados.

        Args:
            data (Dict[str, Dict]): Diccionario con los datos de las imágenes (ID como clave, metadatos y ruta como valor).
        """
        self.data = data

    def list_images(self) -> None:
        """Muestra todas las imágenes disponibles."""
        if not self.data:
            print("No hay imágenes registradas.")
            return
        print("\nImágenes disponibles:")
        for image_id, info in self.data.items():
            print(f"ID: {image_id}, Path: {info.get('path', 'N/A')}, Metadata: {info.get('metadata', {})}")

    def delete(self, image_id: str) -> bool:
        """
        Elimina una imagen y sus metadatos según su ID, incluyendo el archivo físico.

        Args:
            image_id (str): Identificador único de la imagen.

        Returns:
            bool: True si la eliminación fue exitosa, False si hubo un error o se canceló.
        """
        try:
            if image_id not in self.data:
                print(f"No se encontró la imagen con ID {image_id}.")
                return False

            image_info = self.data[image_id]
            file_path = image_info.get("path", "")
            print(f"¿Está seguro de eliminar la imagen {image_id}? (s/n)")
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
            del self.data[image_id]
            print(f"Imagen {image_id} eliminada exitosamente del sistema.")
            return True

        except PermissionError:
            print(f"Error: No se tienen permisos para eliminar el archivo {file_path}.")
            return False
        except Exception as e:
            print(f"Error al eliminar la imagen: {str(e)}")