from django.shortcuts import render
from django.http import HttpResponse
import plotly as plt
import seaborn as sns
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


def home(request):
    # Variable qui récupère le CSV
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    dtype={"fips": str})


    # Variable initialise la fonction choropleth_map avec les paramètres de la map
    fig = px.choropleth_map(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           map_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                       )
    
    # Gère l'affichage avec l'espacement
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # Affiche la map
    fig.show()
    # Retourne reponse HTTP lié à la route avec string "Hello world!"
    return HttpResponse("Hello world!")




