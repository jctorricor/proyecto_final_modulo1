class File:
    
    def __init__(self):
        """
        Constructor de la clase File, inicializa el diccionario images
        
        """
        self.images = {}
    
    def _data_load(self, images_dir):
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
        
        try:
            os.chdir(os.path.join(curr_dir, images_dir))
        except Exception as e:
            print("No existe la ruta especificada favor corriga el error:")
            print("\nERROR: ", e, "\n")
        
        curr_dir = os.getcwd()
        print("Loading files........")
        
        try:
            for file in os.listdir(curr_dir):
                file_name = os.path.splitext(file)
                lista = file_name[0].split("-")
                id = lista[1]
                extension = file_name[1][1:]            
                ruta = os.path.join(curr_dir, file)            
                tamaño = os.path.getsize(ruta)
                self.images[id] = {"id": id, 
                                "filename": file, 
                                "extension": extension, 
                                "path": ruta, 
                                "size": tamaño}            
                print(file, "File Loaded ")
        except Exception as e:
            print("No se pudo leer la ruta especificada:")
            print("\nERROR: ", e, "\n")
    
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
            print("Se genero un error...........")
            print("\nERROR: ", e, "\n")
        
        return resultado
            
        
                
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
    file._data_load('../covid/images')
    file.show_data()