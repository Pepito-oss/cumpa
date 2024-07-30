import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Configuración de Streamlit
st.title('Análisis de Datos de Automóviles')

# Cargar el archivo CSV usando el cargador de archivos de Streamlit
archivo_csv = st.file_uploader("Sube tu archivo CSV", type="csv")

if archivo_csv:
    try:
        # Cargar los datos
        data = pd.read_csv(archivo_csv)

        # Mostrar las primeras filas del dataset
        st.write(data.head())

        # Función para graficar y mostrar gráficos en Streamlit
        def plot_and_show(data, x, y, title, xlabel, ylabel, plot_type='line', color='blue'):
            plt.figure(figsize=(10, 6))
            if plot_type == 'line':
                sns.lineplot(x=x, y=y, data=data, color=color)
            elif plot_type == 'bar':
                sns.barplot(x=x, y=y, data=data, color=color)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            st.pyplot(plt.gcf())
            plt.close()

        # Visualización de datos generales
        plot_and_show(data, 'model', 'price', 'Precio de Automóviles por Modelo', 'Modelo', 'Precio', 'bar', 'teal')
        plot_and_show(data, 'model', 'performance', 'Rendimiento por Modelo', 'Modelo', 'Rendimiento', 'bar', 'coral')
        plot_and_show(data, 'model', 'km', 'Kilometraje por Modelo', 'Modelo', 'Kilometraje', 'bar', 'green')
        plot_and_show(data, 'model', 'age', 'Edad de los Dueños por Modelo', 'Modelo', 'Edad', 'bar', 'orange')

        # Seleccionar un modelo para el análisis de regresión lineal
        modelos = data['model'].unique()
        modelo_seleccionado = st.selectbox("Selecciona un modelo", modelos)

        # Filtrar datos para el modelo seleccionado
        data_modelo = data[data['model'] == modelo_seleccionado]

        if not data_modelo.empty:
            # Realizar la regresión lineal (en este caso, predicción de precio en función de km)
            X = data_modelo[['km']].values
            y = data_modelo['price'].values

            # Ajustar modelo de regresión lineal
            model = LinearRegression()
            model.fit(X, y)
            predictions = model.predict(X)
            r2 = r2_score(y, predictions)

            # Graficar la regresión lineal
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='km', y='price', data=data_modelo, color='blue')
            sns.lineplot(x=data_modelo['km'], y=predictions, color='red')
            plt.title(f'Regresión Lineal: Precio en función de Kilometraje para {modelo_seleccionado}')
            plt.xlabel('Kilometraje')
            plt.ylabel('Precio')
            plt.grid(True)
            st.pyplot(plt.gcf())
            plt.close()

            # Mostrar el valor de R²
            st.write(f'Precisión de la regresión lineal (R²) para {modelo_seleccionado}: {r2:.2f}')
        else:
            st.warning("No hay suficientes datos para realizar la regresión lineal.")

    except pd.errors.EmptyDataError:
        st.error("El archivo está vacío. Por favor, verifique el contenido del archivo.")
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
