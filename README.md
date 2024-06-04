<h1 align="center"> Exámen Final Módulo 2 </h1>

Este proyecto permite crear una aplicación web simple, ligera, flexible para Python, en la que puede comparar dos textos de forma rápida y sencilla, insertando parámetrtos iguales en donde el resultado es mismos textos, también tiene el botón que permite rergresar al inicio del formulario e ingresar parámetros diferentes, y el resultado es textos diferentes. Puede realizarlo cuantas veces lo desee.

> <h1 align="center"> Requisitos Técnicos </h1>

En éste caso la aplicación fue desarrollada en la plataforma de AWS, entonces:

1. Configurar la instancia EC2 con Amazon Linux, crear clave.pem, configurando el cortafuegos y seguridad para proteger la aplicación, abriendo solamente los puertos necesarios, en este caso el puerto 5000.

2. Crear el entorno (IDE) Cloud9, configurar las herramientas de desarrollo en la instancia e instalar Python, Git y despliega.

> <h1 align="center"> Desarrollo de la Aplicación Web </h1>

**Abrimos el entorno Cloud9 :**
- [x] Para dar permisos a la clave.pem y asociar la EC2 con el Cloud9, ejecutamos el comando:

     :shipit: chmod 600 calve.pem

     :shipit: ssh -i clave.pem ec2-user@IP_pública_EC2

- [x] Para actualizar las librerías, ejecutamos el comando:

     :dizzy: sudo yum update

- [x] Para instalar Python3 y comprobar la versión del mismo, ejecutamos los comandos:

     :snake: sudo yum install python3

     :snake: python3 –-version

- [x] Para instalar pip, ejecutamos el comando:

     :baby_chick: sudo yum install python3-pip

- [x] Para instalar Flask, ejecutamos el comando:

     :cyclone: pip install Flask
