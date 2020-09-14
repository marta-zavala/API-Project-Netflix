import functions as fn
import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Cleaning data
def data():
    df=pd.read_csv('../Input/netflix_titles.csv')
    netflix=df[['type','title','country','release_year','duration','listed_in','description']]
    # Por restriccion de la API me quedo con 1000 filas, para ello elimino los TV Shows y me quedo solo con peliculas de United States posteriores a 1995.
    netflix=netflix[netflix.type=='Movie']
    netflix=netflix[netflix.country=='United States']
    netflix=netflix[netflix.release_year>1995]
    # Me quedan 1300 resultados, me quedo con los 1000 primeros.
    netflix=netflix.head(1000)
    # ApiKeys de rapidapi y The Movie Database
    apiKey = os.getenv("API_IH")
    rapidapiKey = os.getenv("RAPIDAPI")
    # Extraigo el ID de las pelis de rapidapi (funcion getID de functions.py)
    netflix['id']=[fn.getID(x,rapidapiKey) for x in netflix['title']]
    netflix = netflix[~(netflix.id == '{"Response":"False","Error":"Movie not found!"}')]
    netflix = netflix[~(netflix.id == '{"Response":"False","Error":"Too many results."}')]
    net=netflix
    # Enriquezco el dataset con info de The movie dataset (funcion getFromTMDB de functions.py)
    for i in ['popularity','vote_count','vote_average']:
        net[f'{i}'] = [fn.getFromTMDB(x,i,apiKey) for x in net['id']]
    # Elimino las pelis que no se han encontrado
    net = net[~(netflix.listed_in == 'Nan')]
    # Exporto el dataset a un csv nuevo en la carpeta output
    net.to_csv("../Output/NetflixFull.csv",index=False)

