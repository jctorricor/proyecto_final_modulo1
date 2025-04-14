import os
from typing import Dict

class DeleteImage:
    """Clase para gestionar la eliminación de imágenes y sus metadatos."""
    
    def __init__(self, images: Dict[str, Dict]):
        """
        Inicializa el gestor de eliminación con los datos de las imágenes.

        Args:
            images (Dict[str, Dict]): Diccionario con datos de imágenes (ID como clave, metadatos como valor).
        """
        self.images = images

    def list_images(self) -> None:
        """Muestra todas las imágenes disponibles."""
        if not self.images:
            print("No hay imágenes registradas.")
            return
        print("\nImágenes disponibles:")
        for image_id, info in self.images.items():
            print(f"ID: {image_id}, Filename: {info.get('filename', 'N/A')}, "
                  f"Extension: {info.get('extension', 'N/A')}, Path: {info.get('path', 'N/A')}, "
                  f"Size: {info.get('size', 'N/A')} bytes")

    def delete(self, image_id: str) -> bool:
        """
        Elimina una imagen y sus metadatos según su ID, incluyendo el archivo físico.

        Args:
            image_id (str): Identificador único de la imagen.

        Returns:
            bool: True si la eliminación fue exitosa, False si hubo un error o se canceló.
        """
        try:
            if image_id not in self.images:
                print(f"No se encontró la imagen con ID {image_id}.")
                return False

            image_info = self.images[image_id]  
            file_path = image_info.get("path", "")
            print(f"¿Está seguro de eliminar la imagen {image_id} ({image_info.get('filename', 'N/A')})? (s/n)")
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
            del self.images[image_id]
            print(f"Imagen {image_id} eliminada exitosamente del sistema.")
            return True

        