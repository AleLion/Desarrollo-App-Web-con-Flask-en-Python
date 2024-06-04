<h1 align="center"> Exámen Final Módulo 2 </h1>

Este proyecto permite crear una aplicación web simple, ligera, flexible para Python, en la que puede comparar dos textos de forma rápida y sencilla, insertando parámetrtos iguales en donde el resultado es mismos textos, también tiene el botón que permite regresar al inicio del formulario e ingresar parámetros diferentes, y el resultado es textos diferentes. Puede realizarlo cuantas veces lo desee. Adicional, cuenta con test de pruebas para verificar el funcionamiento correcto de la aplicación.


> <h1 align="center"> Requisitos Técnicos </h1>

En éste caso la aplicación fue desarrollada en la plataforma de AWS, entonces:

1. Configurar la instancia EC2 con Amazon Linux, crear clave.pem, configurando el cortafuegos y seguridad para proteger la aplicación, abriendo solamente los puertos necesarios, en este caso el puerto 5000.

2. Crear el entorno (IDE) Cloud9, configurar las herramientas de desarrollo en la instancia e instalar Python, Git y despliega.
   

**Abrimos el entorno Cloud9 :**


:shipit: Para dar permisos a la clave.pem y asociar la EC2 con el Cloud9, ejecutamos el comando:

     chmod 600 clave.pem

     ssh -i clave.pem ec2-user@IP_pública_EC2

:shipit: Para actualizar las librerías, ejecutamos el comando:

     sudo yum update


:snake: Para instalar Python3 y comprobar la versión del mismo, ejecutamos los comandos:

     sudo yum install python3

     python3 –-version

:baby_chick: Para instalar pip, ejecutamos el comando:

     sudo yum install python3-pip

 *Este software permite instalar el Flask*

:cyclone: Para instalar Flask, ejecutamos el comando:

      pip install Flask     
      
*Este software permite desarrollar y desplegar la aplicación*

> <h1 align="center"> Desarrollo de la Aplicación Web </h1>

**Continuamos en el entorno Cloud9 :**

>> Ejecutamos el comando nano app.py ... pegamos el código.

>>Ejecutamos el comando nano test.py ... pegamos el código. *Este permite realizar pruebas automatizadas*

>> Creamos el directorio **templates**, ingresamos, creamos los ficheros form.html y result.html.

>> Ejecutamos el comando python3 app.py.    *Permite desplegar la aplicación.*

>> Vamos a la EC2, copiamos la IP pública, abrimos el navegador y pegamos la IP_pública:5000

:sunflower: ...En este punto, la aplicación web ya está desplegada y funciona...:sunflower:



