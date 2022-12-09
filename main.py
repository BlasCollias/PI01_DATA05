#Importamos esta clase que nos permitirá crear una aplicación, que luego se va a encargar de responder las consultas que el cliente le hace al servidor
from fastapi import FastAPI 
import pandas as pd
from pydantic import BaseModel
from typing import Union

app= FastAPI(title= 'Proyecto Individual',
                description = 'Estamos explorando FastAPI',
                VERSION = '1.0.1')

#Voy a crear mi DF, importando el csv
films_df = pd.read_csv("Datasets/films_df_final.csv")


 #1.Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season]) 
@app.get("/get_max_duration/")
async def get_max_duration(año:int, plataforma:str, tipo:str):
    df3= films_df[((films_df['Plataforma'] == plataforma) & (films_df['año_lanzamiento'] == año)& (films_df['tipo_film'] == tipo))]
    maximo= df3.duracion.max()
    film = df3[df3.duracion == maximo]['titulo']

    return 'El film de mayor duración es '+ film

#2-Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)
@app.get("/Cantidad de films por plataforma/")
async def get_count_plataforma(plataforma:str):
    a= films_df[(films_df['Plataforma'].str.contains(plataforma) & (films_df['tipo_film'].str.contains('Movie')))].shape[0]
    b= films_df[(films_df['Plataforma'].str.contains(plataforma) & (films_df['tipo_film'].str.contains('TV Show')))].shape[0]
    return a,b

#3-Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
@app.get('/Cantidad de veces que se repite un genero y plataforma/')
async def get_listedin(genero:str):

    a=films_df[films_df['generos'].str.contains(genero) & (films_df['Plataforma'] == 'Amazon Prime')].shape[0]
    b=films_df[films_df['generos'].str.contains(genero) & (films_df['Plataforma'] == 'Disney Plus')].shape[0]
    c=films_df[films_df['generos'].str.contains(genero) & (films_df['Plataforma'] == 'Hulu')].shape[0]
    d=films_df[films_df['generos'].str.contains(genero) & (films_df['Plataforma'] == 'Netflix')].shape[0]
    
    maximo = max(a,b,c,d)
    if maximo == a:
        plataforma = 'Amazon Prime'
    elif maximo == b:
        plataforma = 'Disney Plus'
    elif maximo == c:
        plataforma = 'Hulu'
    elif maximo == d:
        plataforma = 'Netflix'


    return 'La plataforma en la que más se repite este género es en '+ plataforma



#4-Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
@app.get("/get_actor/")
async def get_actor(plataforma:str,año_lanzamiento:int):
     filtro= films_df[(films_df['Plataforma'].str.contains(plataforma) & (films_df['año_lanzamiento'] == año_lanzamiento))]
     acts = filtro['actores'].str.split(',', expand= True).stack()
     acts = acts.reset_index(level = 1, drop=True).rename('actors')