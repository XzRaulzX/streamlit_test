import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Seguimiento de Gastos Mensuales",
    page_icon=":money_with_wings:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y subtítulo de la aplicación
st.title('Seguimiento de Gastos Mensuales')
st.subheader('Visualiza tu presupuesto y gastos a lo largo del año')

# Parámetros de entrada
st.sidebar.header('Ajustes del Presupuesto')
presupuesto_mensual = st.sidebar.number_input('Presupuesto Mensual (USD)', min_value=100, max_value=10000, value=2000, step=100)

# Parámetros de entrada para gastos
st.sidebar.header('Gastos Mensuales')
gasto_alimentos = st.sidebar.number_input('Gasto en Alimentos (USD)', min_value=0, max_value=5000, value=500, step=50)
gasto_vivienda = st.sidebar.number_input('Gasto en Vivienda (USD)', min_value=0, max_value=5000, value=800, step=50)
gasto_transporte = st.sidebar.number_input('Gasto en Transporte (USD)', min_value=0, max_value=2000, value=200, step=50)
gasto_entretenimiento = st.sidebar.number_input('Gasto en Entretenimiento (USD)', min_value=0, max_value=2000, value=100, step=50)
gasto_otros = st.sidebar.number_input('Otros Gastos (USD)', min_value=0, max_value=2000, value=200, step=50)

# Parámetros para los labels
st.sidebar.header('Ajustes de Labels')
titulo_grafico = st.sidebar.text_input('Título del Gráfico', 'Gastos Mensuales vs Presupuesto')
label_x = st.sidebar.text_input('Label del Eje X', 'Meses')
label_y = st.sidebar.text_input('Label del Eje Y', 'Gastos (USD)')

# Calcular el gasto total por mes
meses = np.arange(1, 13)
gastos_totales = gasto_alimentos + gasto_vivienda + gasto_transporte + gasto_entretenimiento + gasto_otros
gastos_mensuales = np.full(12, gastos_totales)
presupuesto = np.full(12, presupuesto_mensual)

# Crear el gráfico interactivo
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(meses, gastos_mensuales, label='Gastos Mensuales', color='r', marker='o')
ax.plot(meses, presupuesto, label='Presupuesto Mensual', color='g', linestyle='--')
ax.fill_between(meses, gastos_mensuales, presupuesto, where=(gastos_mensuales > presupuesto), color='red', alpha=0.3, interpolate=True, label='Exceso de Gasto')
ax.fill_between(meses, gastos_mensuales, presupuesto, where=(gastos_mensuales <= presupuesto), color='green', alpha=0.3, interpolate=True, label='Dentro del Presupuesto')

ax.set_title(titulo_grafico)
ax.set_xlabel(label_x)
ax.set_ylabel(label_y)
ax.legend()
st.pyplot(fig)

# Información adicional
st.markdown('---')
st.markdown('### Información Adicional')
st.markdown('Esta aplicación permite calcular y visualizar los gastos mensuales en comparación con el presupuesto definido, ajustando los parámetros de gasto para ver cómo cambia la gráfica en tiempo real.')

# Créditos y enlaces
st.markdown('---')
st.markdown('#### Acerca del Autor')
st.markdown('Desarrollado por [Tu Nombre](https://github.com/tu-usuario)')
