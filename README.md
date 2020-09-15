# Project 3: API Project

![alt text](https://www.elplural.com/uploads/s1/62/52/27/logotipo-de-netflix_4_800x450.jpeg)

Este proyecto parte de un dataset de películas de Netflix "Kaggle"(https://www.kaggle.com/shivamb/netflix-shows), el cual se ha enriquecido con información de la API TMDB(https://www.themoviedb.org/documentation/api)


## 1. Steps

1. Escoger el dataset
2. Enriquecer el dataset con info adicional, mediante dos pasos:
    - Primero se ha obtenido el ID de las películas del dataset realizando una requests a la API Rapidapi(https://rapidapi.com/)
    - Con el ID de cada película se ha extraido la información adicional de la API TMDB(https://www.themoviedb.org/documentation/api).
3. Iniciamos el programa en la terminal
4. Gracias a la biblioteca argparse, se han guardado las variables introducidas por teclado por el usuario
5. El programa devuelve información extraida del dataset en función de los parámetros introducidos

## 2. Cómo ejecutar el programa

Para llamar al programa desde la terminal hay que llamar al archivo main.py e introducir los parámetros que posteriormente se van a emplear para extraer la info. 
Para recibir información sobre los parámetros a introducir debe ejecutar '~python3 main.py -h'
Estos parámetros son:
- -t : Título de la película. Debe ser introducido entre comillas con el mismo nombre que aparece en la plataforma de Netflix en inglés.
- -g : Género de la película. Si llama a la función 'main.py -h' mostrará una lista con algunas de las opciones permitidas.
- -y : Año de estreno
- -r : Valoración de la película
A todos los parámetros se les han introducido valores por defecto, de manera que si no introduces nada y solo llamas a la función main.py, no se realizará ningún filtro en el dataset y devolverá directamente el top películas ordenadas de mejor a peor rating.


## 3. Return
En función de los parámetros introducidos puedes obtener:
- Título: Devuelve la información sobre la película introducida y la diferencia entre su rating y la media de las valoraciones de todo el dataset.
    - Ejemplo:    ~python3 main.py -t "Charlie's Angels: Full Throttle"
- Género, año y rating: Puedes introducir uno de ellos, dos o los tres. Devuelve el top 5 películas filtradas por los parámetros introducidos ordenados de mejor a peor rating.
    - Ejemplo:    ~python3 main.py -g "Dramas" -y 1997 -r 8         ~python3 main.py -y 2015 -r 7
- Sin parámetros: Top películas ordenadas de mejor a peor rating (dataset sin filtrar).
    - Ejemplo:    ~python3 main.py

## 4. Recursos empleados:
- Python
- Pandas
- Requests
- Argparse
- Subprocess
