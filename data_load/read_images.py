class File:
    
    def __init__(self):
        """
        Constructor de la clase File, inicializa los diccionarios images y metadata.
        """
        self.images = {}  # Mantener por compatibilidad, pero no se usa
        self.metadata = {}  # Inicializar metadata
    
    def _get_config_path(self):
        """
        Obtiene el directorio de trabajo actual.
        """
        import os 
        return os.getcwd()

    def _data_process(self, path, type_recurso=1):
        """
        Procesa archivos o directorios y actualiza los metadatos.

        Parameters
        ----------
        path: str
            Ruta al archivo o directorio a procesar.
        type_recurso: int
            Tipo de recurso a procesar (1: archivo, 2: directorio).

        Returns
        -------
        bool: True si el procesamiento fue exitoso, False si hubo error.
        """
        import os

        try:
            if type_recurso == 2:  # Directorio
                for file in os.listdir(path):
                    file_path = os.path.join(path, file)
                    if os.path.isfile(file_path):
                        self.metadata[file] = {
                            'filename': file,
                            'path': file_path,
                            'size': os.path.getsize(file_path),
                            'last_modified': os.path.getmtime(file_path)
                        }                        
                return True
            
            elif type_recurso == 1:  # Archivo
                if os.path.isfile(path):
                    filename = os.path.basename(path)
                    self.metadata[filename] = {
                        'filename': filename,
                        'path': path,
                        'size': os.path.getsize(path),
                        'last_modified': os.path.getmtime(path)
                    }                    
                    return True
                return False
            
            else:
                return False
                
        except Exception as e:
            print("No se pudo leer la imagen: ", path, type_recurso)
            print("\nERROR: ", e, "\n")
            return False

    def _data_load(self):
        """
        Carga los datos iniciales de las imágenes desde covid/images y covid/nuevo.
        """
        import os
        
        curr_dir = os.getcwd()
        print("Loading files........")
        for folder in ["covid/images", "covid/nuevo"]:
            path = os.path.join(curr_dir, folder)
            if os.path.exists(path):
                print("RUTA A LEER ARCHIVOS: ", path)
                self._data_process(path, 2)
    
            
    def _del_file_procesado(self, pathfile):
        """
        Copia un archivo a covid/images y elimina el original.

        Parameters
        ----------
        pathfile: str
            Ruta del archivo a procesar.
        """
        import os
        import shutil

        if os.path.exists(pathfile):
            try:
                ruta_images = os.path.join(os.getcwd(), 'covid/images')
                filename = os.path.basename(pathfile)
                destino = os.path.join(ruta_images, filename)
                shutil.copy2(pathfile, destino)
                os.remove(pathfile)
                self._data_process(ruta_images, 2)  # Actualizar metadatos
            except Exception as e:
                print("ERROR: ", e)

    def show_data(self):
        """
        Muestra los datos de los metadatos de las imágenes.
        """
        try:
            if not self.metadata:
                print("No hay datos para mostrar.")
                return
            for filename, data in self.metadata.items():
                print(f"filename: {filename}, "
                      f"path: {data['path']}, "
                      f"size: {data['size']} bytes, "
                      f"last_modified: {data['last_modified']}")
        except Exception as e:
            print("ERROR: ", e)
            
if __name__ == "__main__":
    file = File()
    file._data_load()
    file.show_data()