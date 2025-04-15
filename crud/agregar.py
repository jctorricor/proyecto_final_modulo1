class ProcessImage:

    def copiar(self):
        import os
        import shutil
        
        while True:
            print("\nPresione 0 para salir\n")
            origen = input("Ingrese la ruta de la imagen a subir: ").strip()
            path = os.getcwd()
            
            proyecto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            destino = os.path.normpath(os.path.join(proyecto_dir, "covid"))
            destino = os.path.normpath(os.path.join(destino, "nuevo"))
            
            try:
                filepath, filename = os.path.split(origen)   
                path_filename = os.path.join(destino, filename)
                shutil.copy(origen, path_filename)
                print(f"\nSuccess Copy: '{origen}' a '{path_filename}'\n")                
                return path_filename                 
            except Exception as e:
                print(f"ERROR en copia: {e}")
                return 'ERROR'                    
            
            if origen == '0':
                return 'SALIR'                        
