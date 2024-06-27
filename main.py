import streamlit as st
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Gráfico de Pastel con Streamlit",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y subtítulo de la aplicación
st.title('Gráfico de Pastel con Streamlit')
st.subheader('Visualiza la distribución de tres variables numéricas')

# Parámetros de entrada para los datos
st.sidebar.header('Ingreso de Datos')
nombre_variable1 = st.sidebar.text_input('Nombre de la Variable 1', value='Empresa 1')
nombre_variable2 = st.sidebar.text_input('Nombre de la Variable 2', value='Empresa 2')
nombre_variable3 = st.sidebar.text_input('Nombre de la Variable 3', value='Empresa 3')

variable1 = st.sidebar.number_input(f'{nombre_variable1}', min_value=0.0, step=0.1, format="%.1f", value=10.0)
variable2 = st.sidebar.number_input(f'{nombre_variable2}', min_value=0.0, step=0.1, format="%.1f", value=20.0)
variable3 = st.sidebar.number_input(f'{nombre_variable3}', min_value=0.0, step=0.1, format="%.1f", value=30.0)


# Crear el gráfico de pastel
labels = [nombre_variable1, nombre_variable2, nombre_variable3]
sizes = [variable1, variable2, variable3]
colors = ['#ff9999','#66b3ff','#99ff99']

fig, ax = plt.subplots(figsize=(6, 3))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Mostrar el gráfico de pastel
st.pyplot(fig)
plt.subplots(figsize=(6, 4))
# Información adicional
st.markdown('---')
st.markdown('### Información Adicional')
st.markdown('Esta aplicación permite visualizar la distribución de tres variables numéricas ingresadas por el usuario en un gráfico de pastel.')

# Créditos y enlaces
st.markdown('---')
st.markdown('#### Acerca del Autor')
st.markdown('Desarrollado por [Raul](https://github.com/XzRaulzX/streamlit_test)')
