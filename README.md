![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)


# PROYECTO INDIVIDUAL 1: Blas Collias

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

# Introducción
La idea del proyecto fue aprender a elaborar y ejecutar una API, mediante la herramienta FastAPI que justamente es conocida por ser de alto rendimiento, rapida, intuitiva y minimizar tanto el código como el error humano. Previamente, fueron provistos un conjunto de archivos de plataformas de films(series y shows de TV) para que nosotros apliquemos el proceso de ETL, el cual voy a explicar los pasos que tomé.

***

## **Proceso ETL**
Extracción, transformación y carga (ETL) es una canalización de datos que se usa para recopilar datos de varios orígenes. Luego, transforma los datos según las reglas de negocio y los carga en un almacén de datos de destino.

[![etl-data-transformation-concept-raw-260nw-1978168019.webp](https://i.postimg.cc/QMBZsfB9/etl-data-transformation-concept-raw-260nw-1978168019.webp)](https://postimg.cc/QBryJkJh)

A continuación, voy a explicar un poco de qué hice en cada paso del proceso.

#### **Entendimiento de los datos**
En principio, obtuvimos un pantallazo de la datos con los que vamos a trabajar. Buscamos comprender las distintas variables, cómo se relacionan, qué tipo de variables nos encontramos, etc. Esto con el fin de tener un mejor entendimiento sobre la data con la que contamos, saber qué herramientas utilizar para su análisis, y obtener mejores respuestas.

#### **Integración de datos**

El primer accionar, fue la integracion de los 4 archivos que estaban contenidos en la carpeta 'Datasets' que nos dieron, los cuales eran 3 en formato csv y uno en formato json. Nos encargamos de transformarlos en dataframes mediante los métodos read_csv/read_json de 'Pandas'(librería de Python).

Utilicé metodos como '.info()', 'shape', entre otros, para ver los tipos de variables y el tamaño de los dataframes por ejemplo.

#### **Limpieza y normalización de Datos**

Empezamos a ver qué datos nos van a ser útiles y cuáles no, para reducir el tamaño de la masa de datos con la que vamos a trabajar. Antes de eliminar algunas columnas, analicé el costo/beneficio de hacerlo, podría haberlas dejado por si en un futuro quería profundizar el análisis de este proyecto. Decidí eliminar 4 columnas por un tema de eficiencia, además de que las columnas eliminadas contenían muchos valores nulos, por lo tanto no era muy buena su calidad.
Por otra parte, renombré todas las columnas ya que estaban en ingles, para facilitar el manejo y el entendimiento de las variables.

#### **Transformación de Datos**

Exporté los dataframes a MySql para poder seguir trabajando con ellos, puliendo detalles, y poder realizar el modelado de datos.

#### **Imputación de valores faltantes**
Tuve que analizar si había, cuántos había y qué hacer con esos valores nulos. Una opción era borrarlos, pero no me pareció la más viable. Como la mayoría de las variables eran categóricas, decidí omitir esos valores nulos rellenandolos con un 'Sin Dato' mediante el método 'fillna()'.


***

## **Creación de la API en un entorno docker**

Creé un ambiente de desarrollo con Docker y Python, y mediante el framework FastAPI facilitamos la creación de la misma. Vale la pena hacerlo para que al desarrollar en nuestra computadora local, los cambios que hago  se vean reflejados dentro del contenedor
Con la documentación que nos dieron de FastaAPI creamos un archivo.py(main.py, donde tenemos nuestra app), el cual lo corrimos con el comando uvicorn main:app (el cual ejecuta la app). En el mismo creamos un objeto('app') y mediante el '--reload' que se usa en la etapa de desarrollo, permitimos que al realizar cambios en el codigo y guardarlos, se reinicie el servidor con los cambios hechos.

En el archivo requirements.txt contiene las dependencias que necesitamos, y ademas instalamos las mismas.

Tenemos una API que recibe HTTP request(envia peticiones a un URL específico y procesa la respuesta).

Creamos tambien un archivo Dockerfile, en el cual ejecutamos la instalación de las dependencias(RUN ...).

Este fue el resultado del desarrollo donde vamos a realizar las consultas:

[![imagen-2023-02-14-155956547.png](https://i.postimg.cc/25YnNK9T/imagen-2023-02-14-155956547.png)](https://postimg.cc/FYPYjD4J)

***
## **Consultas**

Ya teniendo el ambiente de desarrollo preparado, procedí a armar las distintas consultas:

-Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

-Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma).

Adjunto imagen con un ejemplo de la 2da consulta. Le preguntamos la cantidad de films de la plataforma Amazon Prime, donde la respuesta fue 7814 películas y 1854 Tv shows.

[![Whats-App-Image-2023-02-14-at-3-37-29-PM.jpg](https://i.postimg.cc/vBN1TqhJ/Whats-App-Image-2023-02-14-at-3-37-29-PM.jpg)](https://postimg.cc/TLn2HcZ0)

-Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

-Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

