import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Análisis de datos de vehículos usados")

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Mostrar histograma si está seleccionada la casilla
if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar scatter plot si está seleccionada la casilla
if build_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs Odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition", title="Dispersión Precio vs Odómetro")
    st.plotly_chart(fig_scatter, use_container_width=True)