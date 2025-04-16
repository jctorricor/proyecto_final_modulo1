class File:
    """
    Gestiona la información (metadatos) sobre archivos dentro de una estructura
    de proyecto específica.

    Permite cargar metadatos de archivos existentes en directorios predefinidos,
    procesar nuevos archivos o directorios para extraer sus metadatos, mover
    archivos entre estados (ej. 'nuevo' a 'procesado') y mostrar los
    metadatos recopilados.

    Atributos:
        images (dict): Mantenido por posible compatibilidad, pero actualmente no utilizado
                       en la lógica principal.
        metadata (dict): Diccionario que almacena los metadatos de los archivos.
                         Las claves son los nombres de archivo (basename) y los
                         valores son diccionarios con detalles como 'path', 'size',
                         'last_modified'.
    """

    def __init__(self):
        """
        Constructor de la clase File.

        Inicializa el diccionario `self.metadata` vacío, que se usará para
        almacenar los metadatos de los archivos procesados. También inicializa
        `self.images`, aunque no se utiliza activamente en los métodos actuales.
        """
        self.images = {}  # Mantener por compatibilidad, pero no se usa
        self.metadata = {}  # Inicializar metadata
    
    def _get_config_path(self):
        """
        Obtiene la ruta absoluta del directorio de trabajo actual.

        Se utiliza internamente como base para construir rutas a los subdirectorios
        específicos del proyecto (ej. 'covid/images', 'covid/nuevo').

        Nota:
            El prefijo '_' indica que este método está destinado a uso interno
            dentro de la clase.

        Returns:
            str: La ruta absoluta del directorio de trabajo actual.
        """
       
        import os 
        return os.getcwd()

    def _data_process(self, path, type_recurso=1):
        """
        Procesa un archivo individual o todos los archivos dentro de un directorio
        y extrae sus metadatos, actualizando el diccionario `self.metadata`.

        Si `type_recurso` es 1, procesa el archivo especificado en `path`.
        Si `type_recurso` es 2, itera sobre todos los archivos dentro del
        directorio `path` y procesa cada uno.

        Los metadatos almacenados para cada archivo incluyen:
        'filename': Nombre base del archivo.
        'path': Ruta completa al archivo.
        'size': Tamaño del archivo en bytes.
        'last_modified': Marca de tiempo (timestamp) de la última modificación.

        Nota:
            El prefijo '_' indica que este método está destinado a uso interno
            dentro de la clase.

        Parameters
        ----------
        path : str
            Ruta al archivo o directorio a procesar.
        type_recurso : int, opcional
            Tipo de recurso a procesar (1: archivo, 2: directorio).
            Por defecto es 1.

        Returns
        -------
        bool
            True si el procesamiento fue exitoso (o parcialmente exitoso en caso
            de directorios), False si se proporcionó un `type_recurso` inválido
            o si ocurrió una excepción durante la lectura de metadatos.
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
        Carga los metadatos iniciales de los archivos encontrados en los
        directorios predefinidos 'covid/images' y 'covid/nuevo'.

        Construye las rutas a estos directorios basándose en el directorio de
        trabajo actual obtenido con `_get_config_path()`. Llama a `_data_process()`
        para cada directorio encontrado para poblar `self.metadata`.

        Nota:
            El prefijo '_' indica que este método está destinado a uso interno
            dentro de la clase. Debería llamarse típicamente después de
            instanciar la clase para cargar el estado inicial.
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
        Mueve un archivo desde su ubicación original (presumiblemente un
        directorio de 'nuevos' o 'pendientes') al directorio 'covid/images'
        y elimina el archivo original.

        Después de mover el archivo, actualiza los metadatos llamando a
        `_data_process` sobre el directorio 'covid/images' para reflejar
        el archivo movido y potencialmente actualizar su información si cambió
        durante la copia (aunque `copy2` intenta preservar metadatos).

        Nota:
            El prefijo '_' indica que este método está destinado a uso interno
            dentro de la clase. El nombre "_del_file_procesado" es ligeramente
            engañoso, ya que la acción principal es *mover* (copiar y luego borrar).

        Parameters
        ----------
        pathfile : str
            Ruta completa del archivo original que se va a mover.
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
        Muestra en la consola los metadatos de los archivos almacenados
        en el diccionario `self.metadata`.

        Itera sobre el diccionario `self.metadata` e imprime la información
        clave de cada archivo (nombre, ruta, tamaño, fecha de modificación).
        Si no hay metadatos cargados, imprime un mensaje indicándolo.
        Formatea la fecha de modificación para que sea más legible.
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