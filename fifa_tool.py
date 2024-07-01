# importamos librerías
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# leer datos
fifa = pd.read_csv("./datos/Fifa 23 Players Data.csv")

#sidebar configuración

with st.sidebar:
    st.write("Este es el sidebar")
    nationality = st.multiselect("Nacionalidad", sorted(fifa["Nationality"].unique()))
    team = st.multiselect("Equipo", sorted(fifa["Club Name"].unique()))
    is_national = st.checkbox("Selección Nacional")
    
#creamos la función de filtrado
def filter_data(df, nationality, team, is_national):
    fifa_copy = df.copy()
    #si la dimension de mi lista es mayor a 0, filtra el df que genere una copia por la columna nacionalidad
    if len(nationality) > 0:
        fifa_copy = fifa_copy[fifa_copy["Nationality"].isin(nationality)]
    #lo mismo para los equipos
    if len(team) > 0:
        fifa_copy = fifa_copy[fifa_copy["Club Name"].isin(team)]
    #la última variable, cuando es true trae la columna national team name 
    if is_national == True:
        fifa_copy = fifa_copy[fifa_copy["National Team Name"] != "-"]
        
    return fifa_copy

#ahora queremos tener un df para mostrar el filtrado
# así que fltramos
fifa_ = filter_data(fifa, nationality, team, is_national)
#para poner titulos
st.title("Fifa 2023")
st.subheader("Análisis de Equpos")
#cuantos juagdores estoy leyendo
total_jugadores = len(fifa_)
#trae la media del overhall
rating_medio = fifa_["Overall"].mean()
#y la media del Value
valor_medio = fifa_["Value(in Euro)"].mean()

#nombramos columnas
col1, col2, col3 = st.columns(3)
#la función metrics es otra forma de mostrar datos, donde los pide label
# :,.0f esto es para el formato del string, que sólo sean enteros, y ponga comas
col1.metric("# Jugadores", f"{total_jugadores:,.0f}")
#:,.1f para que maneje floats
col2.metric("Rating Medio", f"{rating_medio:,.1f}")
col3.metric("Valor $ Medio", f"{valor_medio:,.0f}")

#para hacer el gráfico de radar y definir cómo va a mostrar la información, creamos función
def get_team_statistics(df):
    #estas son las métricas que usamos
    radar_columns = ["Pace Total", "Shooting Total", "Passing Total", "Dribbling Total", "Defending Total", "Physicality Total"]
    
    metrics = []
    for metric in radar_columns:
        metrics.append(fifa_[metric].mean())
    #theta es el nombre de las columnas    
    return pd.DataFrame(dict(metrics=metrics, theta = radar_columns))


#para renderizarlo, creamos la figura
radar_fig = px.line_polar(get_team_statistics(fifa_), r = "metrics", theta="theta", line_close=True)

# Configurar el diseño del gráfico de radar
radar_fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
)

st.plotly_chart(radar_fig)

st.dataframe(fifa_)