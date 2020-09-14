import pandas as pd
import numpy as np
from dotenv import load_dotenv
load_dotenv()
import requests
import os


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