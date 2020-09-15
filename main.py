from argparse import ArgumentParser
import pandas as pd
import numpy as np
import sys
import src.chineseWork as fn
from src.data import *
import subprocess

parser = ArgumentParser(description = "Accede a información sobre las películas de Netflix")
parser.add_argument("-t" "--title",dest="title",type=str,help="Escribe el título de una película de la que quieras obtener información (Entre comillas 'titulo')", default='None',required=False)
parser.add_argument("-y" "--year",dest="year",type=int,help="Escribe el año del que deseas obtener las peliculas mejor valoradas",default=1995,required=False)
parser.add_argument("-g" "--genre",dest="genre",type=str,help="Introduce el género que desea:\n - Stand-Up Comedy\n - Documentaries\n - Children & Family Movies\n - Dramas\n - Dramas, Independent Movies\n - Children & Family Movies, Comedies\n - Horror Movies\n - Action & Adventure\n - Thrillers",default='None',required=False)
parser.add_argument("-r" "--rating",dest="rating",type=int,help="Introduce el rating mínimo deseado(valor entre 0-9)",default=0,required=False)
args = parser.parse_args()

try:
    dataGet(args.title,args.genre,args.rating,args.year)
except FileNotFoundError as e:
    print('Ups... parece ser que todavía no tenemos datos! Prepara tus palomitas mientras esperas a que el programa busque la información y vuelve a ejecutarlo.\nGracias y lo sentimos por la espera.')
    subprocess.run(["say",f'Ups... parece ser que todavía no tenemos datos! Prepara tus palomitas mientras esperas a que el programa busque la información y vuelve a ejecutarlo. Gracias y lo sentimos por la espera.'])
    dataClean()

