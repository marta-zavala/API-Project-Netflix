import pandas as pd
import numpy as np
from dotenv import load_dotenv
load_dotenv()
import requests
import os
from statistics import mean


# Con esta funcion consigo un ID de cada pelicula que extraigo de rapidapi y me servira para sacar informacion de la api The Movie Database
def getID(titulo, key):
    try:    
        url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
        querystring = {"page":"1","r":"json","s":titulo}
        headers = {'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",'x-rapidapi-key': key}
        response = requests.request("GET", url, headers=headers, params=querystring)
        response=(response.text)
        response=((response.replace(' ','').replace('"imdbID":'," ").replace(',"Type":',' ').split())[1]).replace('\"',"")
    except:pass
    return(response)


# Con esta funcion enriquezco el dataset con info de The moivie dataset
def getFromTMDB(id_tmdb,i,key):
    try:
        res = (requests.get(f"https://api.themoviedb.org/3/movie/{id_tmdb}?api_key={key}&language=en-US")).json()[f'{i}']
    except:
        res = 'NaN'
    return res


# Filtra el dataset por genre, year y rating y devuelve los resultados mejor valorados
def propuesta_peli(genre,year,rating,n,df):
    filterinfDataframe = df[(df['Genre'] == f"{genre}") & (df['Year'] >= year) & (df['Rating'] >= rating)].sort_values(by=['Rating'],ascending=False).head(n)
    #filterinfDataframe = filterinfDataframe if n< filterinfDataframe.shape[0] else filterinfDataframe.head(n)
    filterinfDataframe = filterinfDataframe.reset_index(drop=True)
    return filterinfDataframe


# Filtra el dataset por year y rating y devuelve los resultados mejor valorados
def propuesta_genpeli(year,rating,n,df):
    filterinfDataframe = df[(df['Year'] >= year) & (df['Rating'] >= rating)].sort_values(by=['Rating'],ascending=False).head(n)
    #filterinfDataframe = filterinfDataframe if n < filterinfDataframe.shape[0] else filterinfDataframe.head(n)
    filterinfDataframe = filterinfDataframe.reset_index(drop=True)
    return filterinfDataframe


# Esta funcion realiza la media de todos los ratings del dataset y muestra la diferencia con la valoracion de la pelicula elegida
def media(title,df):
    media=round(df.Rating.mean(),1)
    rat=int(df[(df.Title == title)].Rating)
    print(f'La media de ratings del dataset es de {media} y el rating de su película es de {rat}')
    if rat > media:
        return print(f'La película elegida está valorada {str(round(rat-media,1))} puntos por encima de la media.')
    else:
        return print(f'La película elegida está valorada {str(round(media-rat,1))} puntos por debajo de la media')
        

    