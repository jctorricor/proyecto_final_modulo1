# Proyecto Final Modulo 1 - Maestria en Ciencia de Datos e Intelegencia Artificial
# Docente: Msc. Edwin Salcedo
Proyecto Final del Modulo I - Maestria en Ciencia de Datos e Inteligencia Artificial

# Diagrama de paquetes
![Diagrama de Paquetes](https://drive.google.com/uc?export=view&id=1tD_UTnKBhfv1WXCMjrgrgXEwIWTuh1uL)

# Dataset utilizado - [COVID-19 Radiograpy Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) 

![Radiografia](https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-1.png)(https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-50.png)(https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-60.png)(https://github.com/jctorricor/proyecto_final_modulo1/blob/main/covid/images/COVID-90.png)

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


# Instalacion del Proyecto

Para instalar el proyecto se debe seguir los siguientes pasos:

1. Instalacion de Python
   Instalar Python desde el sitio oficial de [Python](https://www.python.org/downloads/)

2. Instalacion de git  
   Instalar git desde el sitio oficial de git [Git](https://git-scm.com/downloads)

3. Clonacion del Proyecto
  $git clone https://github.com/jctorricor/proyecto_final_modulo1.git

4. Ejecucion 
   La ejecion de sistema se lo debe realizar una vez clonado el proyecto e ingresando dentro del directorio que contiene el proyecto por ejemplo proyecto_final_modulo1 ahi dentro ejecutar:
   
   $ python init.py


# Utilizacion del Proyecto
   En este punto se describe como podria utilizar el software implementado para la gestion de radiografias de COVID-19 para lo cual se describen las funcionalidades:

1. Menu inicial

   Al ejecutar el sistema muestra un menu donde el usuario podria seleccionar una de las siguientes opciones:
   1. Agregar 
   2. Modificar
   3. Eliminar
   4. Mostrar
   5. Salir

   A continucacion describiremos uno a uno las opciones del menu:
   1. Agregar 
   
      Permite agregar una nueva imagen a la base de datos de COVID-19 donde el usuario envia la direccion de la imagen a cargar como se muestra en el siguiente ejemplo:

      ------------------------------------------------------

      Gestionar imagenes de COVID-19 Radiography Database:

          1: Agregar nueva imagen
          2: Modificar imagen
          3: Eliminar imagen
          4: Mostrar imagenes cargadas
          0: Salir

      ------------------------------------------------------
      Opcion: 1

      Presione 0 para salir

      Ingrese la ruta de la imagen a subir: /home/juancarlos/test_images/COVID-500.png

      Una vez proporcionado la ruta absoluta de la imagen el sistema proceso de cargar los metadatos de la imagen en nuestra base de datos y asi como tambien se realiza una copia del archivo hacia la ruta definida dentro del sistema como salida el sistema muestra el siguiente mensaje en caso de exito.

      SUCCESS COPY: '/home/juancarlos/test_images/COVID-500.png' a '/home/juancarlos/proyecto_final_modulo1/covid/nuevo'
      /home/juancarlos/proyecto_final_modulo1/covid/nuevo/COVID-500.png
      COVID-500.png File Loaded 
   


