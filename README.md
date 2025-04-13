# proyecto_final_modulo1
Proyecto Final del Modulo I - Maestria en Ciencia de Datos e Inteligencia Artificial

# Diagrama de paquetes
![Diagrama de Paquetes](https://drive.google.com/uc?export=view&id=1tD_UTnKBhfv1WXCMjrgrgXEwIWTuh1uL)


# Módulo modificar.py
Descripción General
modificar.py es un modulo de los 3 requeridos para el proyecto (Agregar, Modificar y eliminar) enfocado en las imágenes médicas COVID-19 y las imagenes nuevas que puedan ser agregadas. Su función principal consiste en renombrar la imagen seleccionada sin alterar su formato.

Características
1. Enfoque Específico
        Opera exclusivamente sobre archivos de imagen en los directorios:
        /covid/images/
        /covid/nuevo/
        Mantiene intactos los formatos originales (.jpg, .png, .dicom, etc.)

2. Diseño Técnico
        La interfaz trabaja por consola 
        Se aplico la arquitectura de tipo modular que permite:
            Uso independiente como script
            Integración con los otros componentes
        Persistencia segura: Operaciones atómicas que no corrompen archivos

3. Flujo del Modulo
    Seleccionar la carpeta donde modificara el nombre
    Se desplegara una lista con los archivos disponibles
    Seleccion del archivo especifico
    Confirmación de cambio de nombre del archivo
    Notificacion del cambio de nombre del archivo
    Preserva extensiones de archivo automáticamente (.jpg, .png)
    Uso de la Biblioteca OS nativa de Python para renombrar el archivo 