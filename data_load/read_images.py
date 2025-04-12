class File:
    
    def __init__(self):
        """Constructor de la clase File, inicializa el diccionario images
        """
        self.images = {}
    
    def _data_load(self, images_dir):
        """Funcion de cargado de datos iniciales sobre las imagenes
            Genera la metadata de los archivos y los guarda en un diccionario de datos        
        """
        import os
        
        curr_dir = os.getcwd()
        os.chdir(os.path.join(curr_dir,images_dir))
        
        curr_dir = os.getcwd()
        print("Loading files........")
        
        for file in os.listdir(curr_dir):
            file_name = os.path.splitext(file)
            lista = file_name[0].split("-")
            id = lista[1]
            extension = file_name[1][1:]            
            ruta = os.path.join(curr_dir,file)            
            tamaño = os.path.getsize(ruta)
            self.images[id] = {"id": id,"filename":file,"extension":extension,"path":ruta,"size":tamaño}            
            print(file,"Loaded")
            
    
    def show_data(self):
        """Funcion que muestra los datos del diccionario relaciondos a imagenes
        """        
        for key,valor in self.images.items():
            print("id:",valor['id']," filename:", valor['filename'], " extension:", valor['extension'], " path", valor['path'], " size:", valor['size'])            
            
            
if __name__ == "__main__":
    file = File()
    file._data_load('../covid/images')
    file.show_data()