# Vehicles
Proyecto Sprint 7
# Análisis de Vehículos Usados - Aplicación Web con Streamlit

Esta aplicación web permite explorar un conjunto de datos de anuncios de venta de vehículos usados en Estados Unidos. Fue desarrollada con Streamlit y utiliza visualizaciones interactivas con Plotly Express.

## Funcionalidad

- Mostrar un **histograma** de la columna `odometer` para analizar la distribución del kilometraje de los vehículos.
- Mostrar un **gráfico de dispersión** que relaciona el precio del vehículo con el kilometraje, coloreado según la condición del vehículo.
- Permite seleccionar qué gráficos visualizar mediante casillas de verificación.
  
Esta herramienta es útil para usuarios que quieran hacer un análisis rápido y visual de los datos de vehículos usados y entender tendencias básicas en el mercado.

## Cómo ejecutar la aplicación

1. Clonar o descargar este repositorio.
2. Asegurarse de tener instalado Python y las librerías necesarias (`streamlit`, `pandas`, `plotly`, `altair`).
3. Ejecutar la aplicación con el comando:
   ```bash
   streamlit run app.py