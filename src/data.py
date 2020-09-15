from src.chineseWork import *
import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import subprocess

# Getting data

def dataGet(title,genre,rating,year):
    df=pd.read_csv('Output/NetflixFull.csv')
    if title!='None':
        print(f'\nInformación sobre {title}:\n')
        subprocess.run(["say",f'A continuación se muestra la información sobre {title}'])
        name = df[(df["Title"]== title)]
        for i in ['Title','Country','Year','Duration','Genre','Description','Popularity','Rating']:
            print(f'{i}: {name[i]}')
        media(title,df)
        return df[df.Title==title]
    elif genre!='None':
        subprocess.run(["say","Introduce el número de películas que desea visualizar"])
        num=int(input("\nIntroduce el número de películas que desea visualizar: "))
        print(f'\nLas {num} películas mejor valoradas del género {genre}, a partir del año {year}, con una puntuación superior a {rating} son:\n')
        subprocess.run(["say",f'\nLas {num} películas mejor valoradas del género {genre}, a partir del año {year}, con una puntuación superior a {rating} son las que se muestran a continuación:\n'])
        return(print(propuesta_peli(genre, year, rating, num, df)))
    elif genre=='None':
        subprocess.run(["say","Introduce el número de películas que desea visualizar"])
        num=int(input("\nIntroduce el número de películas que desea visualizar: "))
        print(f'\nLas {num} películas mejor valoradas a partir del año {year}, con una puntuación superior a {rating} son:\n')
        subprocess.run(["say",f'\nLas {num} películas mejor valoradas a partir del año {year}, con una puntuación superior a {rating} son las que se muestran a continuación:\n'])
        return(print(propuesta_genpeli(year,rating,num,df)))




# Cleaning data

def dataClean():
    df=pd.read_csv('Input/netflix_titles.csv')
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
    netflix['id']=[getID(x,rapidapiKey) for x in netflix['title']]
    netflix = netflix[~(netflix.id == '{"Response":"False","Error":"Movie not found!"}')]
    netflix = netflix[~(netflix.id == '{"Response":"False","Error":"Too many results."}')]
    net=netflix
    # Enriquezco el dataset con info de The movie dataset (funcion getFromTMDB de functions.py)
    for i in ['popularity','vote_count','vote_average']:
        net[f'{i}'] = [getFromTMDB(x,i,apiKey) for x in net['id']]
    # Elimino las pelis que no se han encontrado
    net = net[~(netflix.listed_in == 'Nan')]
    # Elimino columnas innecesarias y renombro columnas
    net=net[['title','country','release_year','duration','listed_in','description','popularity','vote_count','vote_average']]
    net.rename(columns={'title':'Title','country':'Country','release_year':'Year','duration':'Duration','listed_in':'Genre','description':'Description','popularity':'Popularity','vote_count':'Vote Count','vote_average':'Rating'},inplace=True)
    # Exporto el dataset a un csv nuevo en la carpeta output
    net.to_csv("Output/NetflixFull.csv",index=False)

