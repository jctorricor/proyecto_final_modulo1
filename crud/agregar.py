class ProcessImage:

    def copiar(self):
        import os
        import shutil
        
        while True:
            print("\nPresione 0 para salir\n")
            origen = input("Ingrese la ruta de la imagen a subir: ").strip()
            path = os.getcwd()
            
            destino = os.path.join(path, 'covid/nuevo')
            print(destino)

            try:
                shutil.copy(origen, destino)
                print(f"SUCCESS COPY: '{origen}' a '{destino}'")
                filepath, filename = os.path.split(origen)   
                path_filename = os.path.join(destino,filename)
                return path_filename                 
            except Exception as e:
                print(f"ERROR en copia: {e}")
                return 'ERROR'                    
            
            if origen == '0':
                return 'SALIR'                        

        