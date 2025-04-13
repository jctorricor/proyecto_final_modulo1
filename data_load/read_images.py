class File:
    
    def __init__(self):
        """
        Constructor de la clase File, inicializa el diccionario images
        
        """
        self.images = {}
    
    def _get_config_path(self):
        import os 

        path = os.getcwd()

    def _data_process(self, path, type_recurso=1):
        """
        Funcion para agregar los datos de los archivos al diccionario
        
        Parameters
        ----------
        path: str
            Ruta al directorio que contiene los archivos a procesar y cargar al diccionario
        type_recurso: int
            tipo de recurso a procesar 
                1 archivo 
                2 directorio

        Returns
        -------
        bool: True/False
            True si es correcto el procesamiento
            False si genero algun error 

        """
        import os

        try:
            if type_recurso == 2:
                for file in os.listdir(path):
                    file_name = os.path.splitext(file)
                    lista = file_name[0].split("-")
                    id = lista[1]
                    extension = file_name[1][1:]            
                    ruta = os.path.join(path, file)            
                    tamaño = os.path.getsize(ruta)
                    self.images[id] = {"id": id, 
                                    "filename": file, 
                                    "extension": extension, 
                                    "path": ruta, 
                                    "size": tamaño}            
                    print(file, "File Loaded ")
                    return True
            
            elif type_recurso == 1:            
                file_name = os.path.splitext(path)
                lista = file_name[0].split("-")
                id = lista[1]
                extension = file_name[1][1:]                                   
                tamaño = os.path.getsize(path)
                pathfile, file = os.path.split(path)
                self.images[id] = {"id": id, 
                                "filename": file, 
                                "extension": extension, 
                                "path": path, 
                                "size": tamaño}            
                print(file, "File Loaded ")
                return True
            else:
                return False
                
        except Exception as e:
            print("No se pudo leer la ruta especificada: ",path, type_recurso)
            print("\nERROR: ", e, "\n")
            return False


    def _data_load(self):
        """
        Funcion de cargado de datos iniciales sobre las imagenes
        Genera la metadata de los archivos y los guarda en un 
        diccionario datos
        
        Parameters
        ----------
        images_dir: str
            Directorio que contiene las imagenes
        
        Returns
        --------
        None: none
            No retorna ningun objeto simplemente carga los datos en un diccionario
                        
        """
        import os
        
        curr_dir = os.getcwd()
        print("Loading files........")
        path = os.path.join(curr_dir, "covid/images")
        self._data_process(path,2)
        
    
    def copy(self, source, destination):
        """
        Funcion que permite copiar un archivo de una ruta especificada 
        a nuestra base de imagenes
        
        Parameters
        ----------
        source: str
            Direccion origen del archivo
        destination: str
            Direccion de destino para el archivo
        
        Returns
        -------
        bool
            True/False en caso de exito True caso contrario False
        """
        import os        
        import shutil
        
        resultado = False
        
        try:
            shutil.copy(source, destination)
            resultado = True
        except Exception as e:
            print("\nERROR: ", e, "\n")
        
        return resultado
            
    def _del_file_procesado(self, pathfile):
        """
        Funcion para eliminar el archivo de la ruta especificada y nombre de archivo

        Parameters
        ----------
        source: str
            Ruta del archivo a procesar
        filename: str
            nombre del archivo a processar
        
        Returns
        -------
        None: none
           sin ningun valor a retornar
           
        """
        import os

        if os.path.exists(pathfile):
            try:
                os.remove(pathfile)    

            except Exception as e:
                print("ERROR: ",e)


    def show_data(self):
        """
        Funcion que muestra los datos del diccionario relaciondos a imagenes
        
        """    
        try:    
            for key, valor in self.images.items():
                print("id:", valor['id'], 
                    " filename:", valor['filename'], 
                    " extension:", valor['extension'], 
                    " path", valor['path'], 
                    " size:", valor['size']
                    )            
        except Exception as e:
            print("ERROR: ", e)
            
if __name__ == "__main__":
    file = File()
    file._data_load()
    file.show_data()