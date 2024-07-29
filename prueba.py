import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Visualización de Datos de Ejercicios de Gimnasio", layout="wide")

# Cargar el archivo Excel
uploaded_file = st.file_uploader("Carga tu archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    # Mostrar los primeros registros del dataframe
    st.write("Primeros registros del dataset:")
    st.dataframe(df.head())

    # Descripción del dataset
    st.write("Descripción del dataset:")
    st.write(df.describe())

    # Gráfico de barras: Distribución de una columna específica (por ejemplo, 'ExerciseType')
    st.write("Distribución de Ejercicios por Tipo:")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='ExerciseType')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Gráfico de dispersión: Relación entre dos variables (por ejemplo, 'Duration' y 'CaloriesBurned')
    st.write("Relación entre Duración y Calorías Quemadas:")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Duration', y='CaloriesBurned', hue='ExerciseType')
    plt.xlabel('Duración (minutos)')
    plt.ylabel('Calorías Quemadas')
    st.pyplot(plt)
    
    # Histograma: Distribución de la duración de los ejercicios
    st.write("Distribución de la Duración de los Ejercicios:")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Duration'], bins=20, kde=True)
    plt.xlabel('Duración (minutos)')
    st.pyplot(plt)

    # Gráfico de correlación: Mapa de calor de correlaciones entre variables numéricas
    st.write("Mapa de Calor de Correlaciones entre Variables Numéricas:")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    st.pyplot(plt)
else:
    st.write("Por favor, carga un archivo Excel para comenzar.")
