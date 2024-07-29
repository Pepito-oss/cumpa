import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("Análisis de Datos de Estudiantes")

# Carga de los datos
student_mat = pd.read_csv('/mnt/data/student-mat.csv')
student_por = pd.read_csv('/mnt/data/student-por.csv')

# Opciones de visualización
st.sidebar.header("Opciones de Visualización")
dataset = st.sidebar.selectbox("Seleccione el conjunto de datos", ("Matemáticas", "Portugués"))

if dataset == "Matemáticas":
    data = student_mat
else:
    data = student_por

# Mostrar los datos
st.write("### Datos Seleccionados")
st.write(data.head())

# Gráfica de correlación
st.write("### Mapa de Calor de Correlación")
corr = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
st.pyplot(plt)

# Gráfica de distribución de las notas finales
st.write("### Distribución de las Notas Finales")
plt.figure(figsize=(10, 6))
sns.histplot(data['G3'], kde=True)
plt.xlabel('Nota Final')
plt.ylabel('Frecuencia')
st.pyplot(plt)

# Gráfica de dispersión entre las notas finales y el tiempo de estudio
st.write("### Dispersión entre Notas Finales y Tiempo de Estudio")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='studytime', y='G3', data=data)
plt.xlabel('Tiempo de Estudio')
plt.ylabel('Nota Final')
st.pyplot(plt)
