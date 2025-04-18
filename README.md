# Proyecto Final Modulo 1 - Maestria en Ciencia de Datos e Intelegencia Artificial
# Docente: Msc. Edwin Salcedo
Proyecto Final del Modulo I - Maestria en Ciencia de Datos e Inteligencia Artificial

# Diagrama de paquetes
![Diagrama de Paquetes](https://drive.google.com/uc?export=view&id=1tD_UTnKBhfv1WXCMjrgrgXEwIWTuh1uL)

# Dataset utilizado - [COVID-19 Radiograpy Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) 

![Radiografia COVID-1.png](https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-1.png)![Radiografia COVID-50.png](https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-50.png)![Radiografia COVID-60.png](https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-60.png)![Radiografia COVID-90.png](https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-90.png)

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
# Módulo agregar.py
Descripción General:
agregar.py es uno de los tres módulos esenciales (Agregar, Modificar y Eliminar) diseñados para la gestión de imágenes médicas relacionadas con COVID-19, así como la incorporación de nuevas imágenes. Su función principal es facilitar la copia de imágenes desde una ubicación especificada por el usuario a un directorio designado dentro del proyecto, preparándolas para su posterior análisis o procesamiento.

Características:
1. Enfoque Específico: Este módulo se concentra en la copia de archivos de imagen a un directorio específico: /covid/nuevo/.
         Compatibilidad de Formatos: Acepta diversos formatos de imagen comunes (.jpg, .png, .dicom, etc.) sin realizar conversiones, preservando la integridad de los datos originales.
         Interfaz: Opera mediante una interfaz de línea de comandos (consola) para solicitar la ruta de origen de la imagen.

2. Diseño Técnico:
        Se ha adoptado una arquitectura modular que permite:
            Utilización independiente como script.
            Integración fluida con los otros módulos del proyecto.
        Operaciones Seguras: Implementa la copia de archivos de forma robusta, minimizando el riesgo de corrupción de datos.
        Clase ProcessImage: Encapsula la lógica de copia de imágenes.

3. Flujo del Módulo:
    Solicitud al usuario de la ruta de la imagen a copiar.
    Validación de la ruta ingresada.
    Copia de la imagen al directorio /covid/nuevo/.
    Notificación al usuario del resultado de la operación (éxito o error).
    Manejo de excepciones para informar errores durante la copia.
    Uso de Bibliotecas:
    Utiliza los módulos os y shutil de la biblioteca estándar de Python para operaciones de manipulación de archivos y directorios, incluyendo la copia de archivos.
    eliminar.py

# Módulo eliminar.py
Descripción General:
eliminar.py es un componente clave dentro del conjunto de herramientas (Agregar, Modificar y Eliminar) para la gestión de imágenes médicas, con un enfoque especial en imágenes relacionadas con COVID-19. Su propósito principal es permitir la eliminación segura de imágenes y sus metadatos asociados del sistema.

Características:
1. Enfoque Específico: Diseñado para operar sobre archivos de imagen ubicados en los directorios /covid/images/ o /covid/nuevo/ (dependiendo de la configuración del proyecto).
         Eliminación Controlada: Requiere confirmación del usuario antes de eliminar un archivo para prevenir eliminaciones accidentales.
         Gestión de Metadatos: Elimina tanto el archivo de imagen físico como su entrada correspondiente en la base de datos de metadatos.
2. Diseño Técnico:
        Se implementó una arquitectura modular para:
            Facilitar el uso independiente del script.
            Permitir una integración sencilla con los otros componentes del sistema.
        Clase DeleteImage: Encapsula la lógica para la eliminación de imágenes y sus metadatos.
        Manejo de Errores: Incorpora manejo de excepciones para gestionar situaciones como archivos no encontrados o problemas de permisos.
3. Flujo del Módulo:
    Presentación de una lista de imágenes disponibles (basada en los metadatos).
    Solicitud al usuario del nombre del archivo a eliminar.
    Confirmación del usuario para proceder con la eliminación.
    Eliminación del archivo físico del sistema.
    Eliminación de la entrada correspondiente en la base de datos de metadatos.
    Notificación al usuario del resultado de la operación (éxito o error).
    Uso de Bibliotecas:
    Utiliza el módulo os de la biblioteca estándar de Python para interactuar con el sistema de archivos, incluyendo la eliminación de archivos.
    Utiliza el módulo typing para el tipado de datos.

# Instalacion del Proyecto

Para instalar el proyecto se debe seguir los siguientes pasos:

1. Instalacion de Python
   Instalar Python desde el sitio oficial de [Python](https://www.python.org/downloads/)

2. Instalacion de git  
   Instalar git desde el sitio oficial de git [Git](https://git-scm.com/downloads)

3. Clonacion del Proyecto

  $ git clone https://github.com/jctorricor/proyecto_final_modulo1.git

4. Ejecucion 
   La ejecion de sistema se lo debe realizar una vez clonado el proyecto e ingresando dentro del directorio que contiene el proyecto por ejemplo proyecto_final_modulo1 ahi dentro ejecutar:
   
   $ python init.py


# Utilizacion del Proyecto
   El comando anterior iniciara la aplicación desplegando un menú con 5 opciones las cuales se inician usando el teclado y los números respectivos

<center>
   ![Diagrama de Paquetes](https://drive.google.com/uc?export=view&id=1TkKL-RtxsJZ4BiWNaJUszR2SYE8AxEyU)
</center>

# Documentacion de Codigo del Proyecto
La documentacion fue genera con  Sphinx y publicadas dentro de paginas de Github donde podra ver en el siguiente enlace: [Documentacion](https://jctorricor.github.io/documentation/index.html)
