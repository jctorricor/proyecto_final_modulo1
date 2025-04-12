class ProcessImage:
    
    def add_images(self, source, destination):
        """
        Funcion para agregar una nueva imagen en base a los datos de origen y destino

        Parameters
        -----------
        source: str
            Direccion origen del archivo
        destination: str        
            Direccion destino de la imagen
        Returns
        -------
        bool
            True/False en caso de exito True caso contrario False
            
        """
        
        print("Se agrego la imagen")

    def copiar(self):
        import os
        import shutil
        
        while True:
            print("Presione 0 para salir")
            origen = input("Ruta de la imagen:").strip()
            os.chdir("../nuevo")
            destino = os.getcwd()
            print(destino)
            
            try:
                shutil.copy(origen, destino)
                print(f"Archivo copiado de '{origen}' a '{destino}'")   
                break                 
            except Exception as e:
                print(f"Error al copiar: {e}")                    
            
            if origen == '0':
                break                        

        