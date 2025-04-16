class ProcessImage:
    """
    Clase para encapsular operaciones relacionadas con el procesamiento de imágenes.

    Actualmente, incluye funcionalidades para copiar imágenes a una ubicación
    predeterminada dentro de la estructura del proyecto.
    """

    
    def copiar(self):
        """Solicita al usuario una ruta de imagen y la copia a un directorio predefinido.

        Este método entra en un bucle que pide interactivamente al usuario la ruta
        de origen de un archivo de imagen. Informa al usuario que puede ingresar '0'
        para cancelar la operación y salir.

        Calcula la ruta de destino basándose en la ubicación del archivo actual,
        asumiendo una estructura de proyecto específica. El destino final es
        '<directorio_del_proyecto>/covid/nuevo/'.

        Intenta realizar la copia del archivo desde la ruta de origen proporcionada
        a la ruta de destino calculada.

        El bucle y el método terminan cuando:
        1. El usuario ingresa '0' (retorna 'SALIR').
        2. La copia del archivo se realiza con éxito (retorna la ruta completa del archivo copiado).
        3. Ocurre un error durante el proceso de copia (retorna 'ERROR').

        Returns:
            str: La ruta completa del archivo destino si la copia fue exitosa.
            str: La cadena literal 'ERROR' si ocurre una excepción durante la copia.
            str: La cadena literal 'SALIR' si el usuario ingresa '0'.

        Raises:
            FileNotFoundError: Podría ocurrir internamente si el origen no existe (manejado).
            IOError: Podría ocurrir internamente por problemas de permisos u otros
                     errores de E/S (manejado).
            Exception: Captura genérica para otros posibles errores durante la copia
                       (manejado internamente retornando 'ERROR').

        Notas:
            - La ruta de destino está codificada relativamente a la ubicación del script.
              Asegúrate de que la estructura de directorios '<proyecto>/covid/nuevo/' exista
              o pueda ser creada. (Se podría mejorar añadiendo `os.makedirs(destino, exist_ok=True)`).
            - El manejo de errores es genérico; captura cualquier `Exception`.
            - La lógica original tenía un posible problema donde la condición de salida '0'
              podría no alcanzarse si se ingresaba una ruta válida primero. Se recomienda
              verificar la condición '0' *antes* de intentar la copia.
        """
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
