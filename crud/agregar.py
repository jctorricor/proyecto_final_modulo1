class ProcessImage:

    def copiar(self):
        import os
        import shutil
        
        while True:
            print("\nPresione 0 para salir\n")
            origen = input("Ingrese la ruta de la imagen a subir: ").strip()
            os.chdir("../nuevo")
            destino = os.getcwd()
            
            try:
                shutil.copy(origen, destino)
                print(f"SUCCESS COPY: '{origen}' a '{destino}'")   
                break                 
            except Exception as e:
                print(f"ERROR: {e}")                    
            
            if origen == '0':
                break                        

        