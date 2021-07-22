# IEASA-pdf-renombre 📝

Cambia el nombre de los archivos PDF enviados por IEASA para poder identificarlos por periodo y cuenca.

Este documento está pensado para guiar al usuario en la instalación y uso del programa para renombrar los archivos PDF de IEASA, en un lenguaje y nivel de detalle destinado al usuario no especializado en software y programación.
Es posible que sea necesaria la participación de su administrador de sistemas para descargar parte del software necesario.

Cualquier consulta acerca de la instalación y uso no dude en usar el canal de contacto brindado en este documento.

## Instalación 🔧

Software necesario:
<ul>
  <li>Python 3.6 o superior 👉 <a href="https://www.python.org/downloads/">descargar</a></li>
  <li>Java para Windows 👉 <a href="https://www.java.com/es/download/ie_manual.jsp">descargar</a></li>
</ul>

Ambos deben estar incluidos en el PATH del sistema. <a href="https://www.java.com/es/download/help/path_es.html">Cómo cambiar variables del sistema</a>

Al momento de instalar python, ofrece la posibilidad de agregarlo al PATH del sistema (opción "Add Python 3.9 to PATH) 👇

![image](https://user-images.githubusercontent.com/84155397/126665001-5b8d2fe9-d690-4f3b-ac5a-45b2f6036e99.png)

Java no ofrece la opción de agregar al PATH al momento de la instalación, por lo que es necesario hacerlo manualmente. El directorio que debe agregarse al PATH (en caso de haber utilizado la carpeta de descarga por defecto):
```
C:\Program Files (x86)\Java\bin
```
## Descarga de archivos 📂
Descargar los archivos de este repositorio y extraer en alguna carpeta de la computadora. <a href="https://github.com/yagopajarino/IEASA-pdf-renombre/archive/refs/heads/main.zip">Descargar</a>

Luego se debe abrir un CMD (Simbolo del sistema) en la carpeta donde están descargados los archivos, para ello:
<ol>
<li>Ctrl + L dentro de la carpeta -> sombrea la barra de directorio en color azul</li>
<li>Borrar lo sombreado en azul</li>
<li>Escribir CMD</li>
<li>Enter</li>
</ol>

Se debe abrir una pantalla como esta 👇

![image](https://user-images.githubusercontent.com/84155397/126667543-787fb8a6-12aa-4a75-a4de-5e9cf466abc7.png)

que en lugar de C:\Users debe tener la ruta de la carpeta donde se descargaron los archivos.

Una vez tenemos el CMD ubicado en la carpeta donde estan los archivos descargados, utilizamos el siguiente comando:
```
pip install -r requirements.txt
```
![image](https://user-images.githubusercontent.com/84155397/126671901-76f11023-a516-4b52-a2da-78e71b291656.png)

Al dar enter, comienza la descarga e instalación de las librerias necesarias.

## Utilización
Al hacer doble click en app.py:
<ol>
  <li>Abre una ventana negra del python launcher</li>
  <li>Pide al usuario un directorio donde estan guardados los archivos PDF que se quieren renombrar, debe ingresarse sin comillas ("")</li>
  <li>Devuelve el numero de PDF leído, seguido por "OK" en caso de haber cambiado el nombre, "error" en caso de no poder cambiarlo</li>
  <li>Al finalizar cierra la ventana del python laucher</li>
</ol>

Dentro del directorio dado al programa crea una carpeta llamada **output**, donde se guardan los archivos PDF renombrados. En caso de no haber podido renombrar algun archivo, lo guarda con el nombre original, de esta manera la carpeta output tiene la misma cantidad de archivos que la carpeta de origen.

## Contacto
En caso de dudas, consutas, mejoras 👉 <a href="www.yagopajarino.com.ar/contact">Get in touch</a>

## Donar :money_with_wings:
Este repositorio es de uso libre bajo licencia MIT pero tu donación ayuda a mantenero y mejorarlo.

<dl>
  <dt>Mercadopago</dt>
  <dd>ARS 100 a traves de mercadopago <a href="https://mpago.la/1ajy5gq">Aquí</a></dd>
  <dd>ARS 500 a traves de mercadopago <a href="https://mpago.la/1ZDRLo4">Aquí</a></dd>
  <dt>MODO</dt>
  <dd>ARS 100 a traves de MODO <a href="https://www.modo.com.ar/coupon/?id=4DMw4lAphaiczkIDm4J7XU">Aquí</a></dd>
  <dd>ARS 500 a traves de MODO <a href="https://www.modo.com.ar/coupon/?id=LTCa2l9PtoqujxnMiGawL">Aquí</a></dd>
</dl>
