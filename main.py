import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título de la aplicación
st.title('Ejemplo de Aplicación Streamlit')

# Descripción de qué es Streamlit
st.markdown("""
Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web interactivas para Machine Learning y Data Science.
Permite a los desarrolladores crear aplicaciones rápidamente con código Python puro.
""")

# Ejemplo de uso de Streamlit Cloud
st.markdown("""
### Streamlit Cloud
Streamlit Cloud es una plataforma que permite a los desarrolladores desplegar y compartir sus aplicaciones Streamlit en la nube de manera sencilla.
Permite colaboración, revisión y acceso desde cualquier lugar.
""")

# Ejemplo de caching y optimización con st.cache_data
@st.cache_data()
def fetch_data():
    # Simulación de carga de datos
    return {'data': 'Datos cargados'}

data = fetch_data()
st.write(f"Datos cargados: {data}")

# Ejemplo de integración con otras herramientas (ej. gráfico simple)
st.markdown("""
### Integración con otras herramientas
A continuación, se muestra un gráfico simple creado con Matplotlib.
""")
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot()

# Ejemplo de componente personalizado (widget interactivo)
st.markdown("""
### Componente Personalizado
A continuación, se muestra un ejemplo de un componente personalizado (widget interactivo).
""")
option = st.selectbox(
    'Selecciona una opción',
    ('Opción 1', 'Opción 2', 'Opción 3')
)
st.write('Has seleccionado:', option)

# Fin de la aplicación
st.markdown("""
---
Hecho con Streamlit. [Ver código en GitHub](https://github.com/XzRaulzX/streamlit_test.git)
""")
